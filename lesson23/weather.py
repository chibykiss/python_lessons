from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather(city = "Lagos"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Weather Conditions ***\n')
    city = input('Enter a city name: ')

    #check for empty input or whitespace
    if not bool(city.strip()):
        city = 'Lagos'
        # print('You must enter a valid city name.')
        # exit()
    weather = get_weather(city)

    print('\n')
    pprint(weather)