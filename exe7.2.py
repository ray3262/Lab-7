import requests
import json


URL_ISS_LOCATION = "http://api.open-notify.org/iss-now.json"
URL_ASTRONAUTS = "http://api.open-notify.org/astros.json"


response_iss = requests.get(URL_ISS_LOCATION)
data_iss = response_iss.json()


response_astros = requests.get(URL_ASTRONAUTS)
data_astros = response_astros.json()


if response_iss.status_code == 200 and response_astros.status_code == 200:
    print("\n🚀 **Текущее местоположение Международной космической станции (МКС)**")
    print(f"Широта: {data_iss['iss_position']['latitude']}")
    print(f"Долгота: {data_iss['iss_position']['longitude']}\n")

    print("👨‍🚀 **Астронавты в космосе сейчас:**")
    print(f"Всего астронавтов: {data_astros['number']}")
    for astronaut in data_astros["people"]:
        print(f"- {astronaut['name']} (Космический корабль: {astronaut['craft']})")
else:
    print("Ошибка при получении данных API.")
