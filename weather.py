from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Torino"):
        
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric&lang=it'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Ottieni condizioni meteo correnti ***\n')

    city =input("Inserisci il nome di una città... \n")

    # controlla se ci sono stringhe vuote o con spazi vuoti
    if not bool(city.strip()):
        city = "Torino"

    weather_data = get_current_weather(city)
    print("")
    pprint(weather_data)