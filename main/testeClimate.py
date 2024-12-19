import requests
import random
from datetime import datetime

cidade = ''

def paraCidade (cidade):
    api_key = "AAAAPPPPIIII_____KKKKEEEEYYYY"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = cidade
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]
        z = x["weather"]

        weather_description = z[0]["description"]

    else:
        random.seed(datetime.now())
        current_temperature = random.randint(0, 44000000)
    return current_temperature

def wheatherapi(city):
    # Substitua 'YOUR_API_KEY' pela sua chave de API
    api_key = '81ea7f503e3c4a3b911114040240912'
    city = 'Itabira Minas Gerais'

    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    response = requests.get(url)
    data = response.json()

    return str(data)