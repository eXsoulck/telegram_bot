import requests
import os

API = os.getenv("API_KEY")

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def weather_info(city: str):
    # complete url address
    complete_url = base_url + "appid=" + API + "&units=metric" + "&q=" + city

    # return response object
    response = requests.get(complete_url)

    # convert to json format data into
    x = response.json()
    if x["cod"] != "404":
        new_d = x["main"]
        current_temp = str(new_d["temp"])
        current_humidity = str(new_d["humidity"])
        return current_temp, current_humidity
    else:
        return None
