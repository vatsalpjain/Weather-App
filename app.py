import os
from dotenv import load_dotenv
from work import convert_location_to_lat_lon, get_weather_by_lat_lon
from gui import ask_for_location, show_weather_data


load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY2 = os.getenv('API_KEY2')


#Here we are asking the user for the location of the city
location_data_list = ask_for_location()


#Here we are converting the location to latitude and longitude
lat_lon_data = convert_location_to_lat_lon(location_data_list[0],location_data_list[1],location_data_list[2],API_KEY2)
lat,lon = lat_lon_data[0],lat_lon_data[1]


#Here we are getting the weather data for the city
weather_data = get_weather_by_lat_lon(lat,lon)


#Here we are printing the weather data
show_weather_data(weather_data)