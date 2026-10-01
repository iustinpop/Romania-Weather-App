##Romania Weather App

An app built in Python that displays current weather data for any city in Romania, using Open-Meteo's Geocoding and Weather APIs along with Streamlit.

#Features

- Search for the current weather of any city in Romania
- Shows the temperature, wind speed, general conditions, and chance of rain
- Handles invalid city and network errors

#Tehnologies 

- Python
- Requests - (https://pypi.org/project/requests/) for API calls
- Streamlit - (https://streamlit.io/) for the web interface
- Open-Meteo - (https://open-meteo.com/) Geocoding and Forecast APIs

#How to run it

- Clone this repo
- Install the dependencies : pip install requests streamlit
- Run the app : streamlit run app.py

#What I learned

This was my first project in Python using external APIs. While building it i learned : 

- How to chain APIs (using the coordonates from the Geocoding API and plugging them into the Forecast API we obtain the live weather)
- Reading and using JSON responses
- Basic error handling with try/except
- Debugging timezone mismatch between the API's data and local time
- Building a plain web interface with Streamlit
- Matching Data across 2 lists using an index

#Limitations

- This weather app is limited to cities in Romania
- Rain probability is provided from  a forecast model so it may not be accurate for short, localized rain events