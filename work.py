import requests
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY2 = os.getenv('API_KEY2')
API_KEY = os.getenv('API_KEY')


def convert_location_to_lat_lon(city_name,state_code,country_code,API_KEY2):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY2}'
    resp = requests.get(url)
    data = resp.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    return lat,lon


def get_weather_by_lat_lon(lat,lon):
    url_main = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    responce =  requests.get(url_main)
    data_main = responce.json()
    return data_main

