# Smart Meteo Assistant

## Overview

Smart Meteo Assistant is a web application that combines real-time weather data with a locally running AI model to provide contextual weather information and personalized recommendations.

The project explores how external APIs and large language models can work together to transform raw data into useful, natural-language responses.

## Features

- Retrieve weather information through an external API.
- Process weather data using Python and Flask.
- Integrate Ollama to generate AI-powered responses.
- Display weather information and recommendations through a web interface.

## Technologies

- **Python** — Backend development.
- **Flask** — Web application framework.
- **HTML, CSS, JavaScript** — Frontend interface.
- **Ollama** — Local AI model integration.
- **Weather API** — Real-time meteorological data.

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Configure the environment**

Create a `.env` file and add the required API credentials according to the configuration used by the application.

**5. Configure Ollama**

Install Ollama and download the AI model required by the application. Make sure Ollama is running before starting the project.

**6. Run the application**

```bash
python app.py
```

## How It Works

1. The application retrieves weather information from an external API.
2. Flask processes the data and prepares the information for the AI model.
3. Ollama generates a contextual response based on the available weather data.
4. The application displays the result through the web interface.

## Learning Objectives

This project was developed to gain practical experience with:

- REST API integration and JSON data processing.
- Backend development with Flask.
- Communication between frontend and backend.
- Local large language model integration.
- Python virtual environments and dependency management.
- Git and GitHub for version control.

## Future Improvements

- Improve the user interface and responsiveness.
- Introduce additional weather-related features.
- Explore integrations with other external APIs.

## Disclaimer

AI-generated recommendations may contain inaccuracies. Weather information depends on the availability and reliability of the external data provider.
