import requests

API_KEY = "18a25794121c8b064a2126e28846f158"  
CITY_NAME = "белгород"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


params = {
    "q": CITY_NAME,
    "appid": API_KEY,
    "units": "metric",  
    "lang": "ru"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    print(f"Погода в {CITY_NAME}: {weather.capitalize()}")
    print(f"Температура: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
else:
    print("Ошибка получения данных. Проверьте API-ключ или название города.")

