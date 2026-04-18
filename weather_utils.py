import requests
import json
import sys

def get_weather(city: str):

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key=7GPZQV9SX6WGL279PS7SC33VM&contentType=json"
    
    res = requests.get(url)
    if (res.status_code != 200):
        raise Exception(f"status code: {res.status_code}")
        sys.exit()

    data = res.json()
    return data

