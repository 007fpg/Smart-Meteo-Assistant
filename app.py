# facciamo il setup importanto tutto il necessario
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
load_dotenv()
import os

#parte complessa: "urllib" contiene diversi moduli python per lavorare con URL e HTTP requests
import json
from urllib.parse import urlencode #per costruire parti degli URL
from urllib.request import urlopen #permette di inviare richieste ai siti web

#setup di flask
#creiamo un oggetto che affidiamo alla variabile "app" mentre
#__name__ è una variabile che identifica il modulo corrente aiutando a riconoscere anche le cartelle
app = Flask(__name__) 

# route è un percorso url che è associato ad una funzione di python; '/' invece indica l'indirizzo standard del sito.

# "@"è un decorator che aggiunge comportamenti alla funzione. per esempio registra /weather nell'app flask.
@app.route('/')

def home():
    return render_template('index.html')

#prende la chiave dell'API dal file .env tramite os e il comando get
API_Key = os.getenv("OPENWEATHER_API_KEY")

#qui vediamo che route Flask deve fare quando il comando "/weather" è eseguito
@app.route("/weather", methods=["POST"]) # qui usiamo sempre post perchè inviamo informazioni 

def weather():

    # qui riceviamo le informazioni con GET dal sito, quelle della città specifica che abbiamo richiesto.
    data = request.get_json() 
    city = data["city"]
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_Key,
        "units": "metric",
        "lang": "en"
    }

    # "with ... as response"    "with" permette di utilizzare una risorsa; "as X"fa si che il valore sia uguale ad una variabile
    # "urlopen(indirizzo)"      manda una richiesta HTTP all'indirizzo indicato
    # f"{...}?{...}"            è una f-string: valore delle espressioni tra parentesi graffe e ? separa l'indirizzo principale dai parametri.
    # "urlencode(params)"       fa si che i parametri vengano trasformati per adattarsi all'URL.
    with urlopen(f"{url}?{urlencode(params)}") as response:

        # mettiamo una variabile uguale ai dati json trasformati in python di response
        weather_data = json.loads(response.read())

    city_name = weather_data["name"]  
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    altitude = weather_data["main"]["sea_level"]
    minimum = weather_data["main"]["temp_min"]
    maximum = weather_data["main"]["temp_max"]

    #--------------------------------------------------------------------------

    from ollama import chat

    prompt = f"""
        Data (city: {city}; temperature: {temperature} C°; weather: {description}; 
        humidity: {humidity}; from sea level: {altitude})
        You are a friendly, knowledgeable travel companion.
        Your job is to give travelers useful, natural-sounding
        advice based on the current weather in their destination.
        Start a new line, with a separated paragraph about a fun fact from this city.
        Follow these rules:
        - Write like a helpful local friend, not a weather reporter.
        - Keep your answer between 60 and 80 words.
        - Give practical advice on clothing and outdoor activities.
        - Adapt your suggestions to the actual weather conditions.
        - Be warm, conversational, and straightforward.
        - Do not use headings, bullet points, or tables.
        - Do not repeat the input data unnecessarily.
        - Do not explain how you interpret the temperature.
        - Never invent historical weather data or forecasts.
        - Do not make up facts about local attractions.
        - Respond in natural English.
    """

    response_ollama = chat(
        model='qwen3.5:4b',
        messages=[{
            'role': 'user', 
            'content': prompt
            }],
        think=False
    )

    advice_ollama = response_ollama.message.content


    #--------------------------------------------------------------------------

    # come JSON_stringify in JS, questo codice trasforma oggetti python in una risposta HTTP con json 
    # così da inviarli nuovamente a JS, per poi mandarli ad html e scriverli
    return jsonify({
        "city": city_name,
        "temperature": temperature,
        "weather": description,
        "advice" : advice_ollama,
        "minimum": minimum,
        "maximum": maximum,
        "humidity": humidity,
        "altitude": altitude
    })


if __name__ == "__main__":
    app.run(debug=True)