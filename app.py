import streamlit as st
import requests

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    51: "Light drizzle",
    61: "Light rain",
    63: "Rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Snow",
    80: "Rain showers",
    95: "Thunderstorm",
}

def get_coordonates(city):
    url="https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1,
        "countryCode": "RO",
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        return None

    place = data["results"][0]
    return place["latitude"], place["longitude"]

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "hourly" : "precipitation_probability",
        "forecast_days" : 1,
        "timezone" : "Europe/Bucharest",
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["current_weather"], data["hourly"]

st.title("Romanian weather forecast")

city = st.text_input("In which city do you want to know the weather: ")

if st.button("Get weather"):
    st.divider()
    if city == "":
        st.write("")
        st.write("Please enter a city name.")
    else:
        try:
            coords = get_coordonates(city)

            if coords is None:
                st.write("")
                st.write("City not found. Please type a city name.")
            else:
                latitude, longitude = coords
                weather, hourly = get_weather(latitude, longitude)
                description = WEATHER_CODES.get(weather["weathercode"], "Unknown")
                st.header(f"Weather in {city.title()}")
                st.write("")
                st.metric("Conditions", f"{description}")
                st.metric("Temperature", f"{weather["temperature"]}°C")
                st.metric("Wind speed", f"{weather["windspeed"]} km/h")

                hour = weather["time"][11:13]
                position = None
                for index, place in enumerate(hourly["time"]):
                    if place[11:13] == hour:
                        position = index
                        break

                if position is not None:
                    rain_chance = hourly["precipitation_probability"][position]
                    st.metric("Chance of rain", f"{rain_chance}%")
                else:
                    st.write("Rain data can't be provided right now.")

        except requests.exceptions.RequestException:
            st.write("Could not connect. Check internet connection and try again.")
st.divider()