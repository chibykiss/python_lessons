import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_curreent_weather():
    print('\n** Get Current Weather Conditions ***\n')

    city = input('\nEnter a city name\n')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'

    #print(request_url)

    weather_data = requests.get(request_url).json()

    #pprint(weather_data)
    print(f'\nCurrent weather in {weather_data["name"]}, {weather_data["sys"]["country"]}:\n')
    print(f'Temperature: {weather_data["main"]["temp"]}°C\n')
    print(f'Feels like: {weather_data["main"]["feels_like"]}°C\n')
    print(f'Weather: {weather_data["weather"][0]["description"]}')


if __name__ == '__main__':
    get_curreent_weather()