//costanti
const searchButton = document.getElementById('search');
const resultParagraph = document.getElementById('result');
const adviceParagraph = document.getElementById('advice');

searchButton.addEventListener("click", async function(){
    resultParagraph.textContent = "loading...";
    adviceParagraph.textContent = "loading...";
    const city = document.getElementById('city_name').value.trim();
    if (city == "") {
        resultParagraph.textContent = "Input a City";
    }

    // "/weather" è una parte del percorso dal server a flask. il nome è ARBITRARIO. possiamo vedere come su python 
    // ritroviamo il comando "/weather", infatti lì viene detto a flask come comportarsi quando è eseguito quel comando.
    // questa è una HTTP request. ci basta solo la parte finale dell'indirizzo perchè utilizza quello del sito attuale.

    const response = await fetch("/weather", {
        method: "POST", 
        //il metodo POST implica che noi inviamo informazioni ad un determinato sito o indirizzo: con GET le prendiamo
        //Se non si scrive nulla allora JS utilizza GET

        //gli HEADERS sono informazioni aggiuntive che accompagnano una richiesta HTTP. Sono però necessari per far sapere,
        //in questo caso, di che tipo di formato sono i dati.
        headers: { 
            "Content-Type": "application/json"
        },

        //abbiamo bisogno di JSON.stringify perchè trasforma un oggetto JS in una stringa json. così che Flask possa interpretarlo come json
        body: JSON.stringify({ 
            city: city 
        })
    });

    // aspetta la risposta di python per mandarla nel paragrafo result. python riceve la città (city) 
    // e restituisce la temperatura, il meteo e la città stessa. se c'è un errore, lo restituisce nel paragrafo result.
    const data = await response.json();

    if (!response.ok) {
        resultParagraph.textContent = data.error;
    return;
    }

    resultParagraph.innerHTML = `
    <h1>${data.city}</h1>
    <h4> Weather: ${data.weather}</h4>
    <br>
    <p> Temperature: <b>${data.temperature} °C</b> &nbsp; Min: <b>${data.minimum} °C</b> &nbsp; Max: <b>${data.maximum} °C </b></p>
    <p> Altitude: <b>${data.altitude} m </b></p>
    <p> Humidity: <b>${data.humidity} % </b></p>
    `;

    adviceParagraph.textContent = `${data.advice}`;
});