"""
Weather App
------------
A simple Python app that fetches current weather data
from OpenWeatherMap using their free API.
"""




import requests;

API_KEY = "8740d87a2fe3a016b694a6ade0379824"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city): #get weather data from the API
    params = { # API parameters
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
         
    response = requests.get(BASE_URL, params=params) # Make the API request

    if response.status_code == 200:      # Check if the request was successful
        data = response.json()
        print_weather(data)
    else:
        print(" Error:", response.status_code, response.json().get("message", ""))  
        


def print_weather(data): # get the weather data function
    city = data["name"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\n Weather in {city}:") #print the weather data
    print(f" Temperature: {temp}°C")
    print(f" Condition: {weather.capitalize()}")
    print(f" Wind Speed: {wind_speed} m/s\n")

if __name__ == "__main__": # This only runs if the script is executed directly
    city = input("Enter city name: ") #Ask user for city name
    get_weather(city)