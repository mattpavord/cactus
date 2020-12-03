from typing import Tuple
import json
import requests
from django.conf import settings

from raincheck.models import Location

WEATHER_API_KEY = settings.WEATHER_API_KEY
GOOGLE_API_KEY = settings.GOOGLE_API_KEY


def get_or_create_location_from_google_api(location_str: str) -> Location:
    url = f'https://maps.googleapis.com/maps/api/geocode/' \
          f'json?address={location_str}&key={GOOGLE_API_KEY}'
    response = requests.get(url)
    data = json.loads(response.content)['results'][0]

    country = ''
    region = location_str
    for address_component in data['address_components']:
        if 'administrative_area_level_2' in address_component['types']:
            region = address_component['long_name']
        if 'administrative_area_level_1' in address_component['types']:
            country = address_component['long_name']
    coordinate_data = data['geometry']['bounds']
    latitude = (coordinate_data['northeast']['lat'] + coordinate_data['southwest']['lat']) / 2
    longitude = (coordinate_data['northeast']['lng'] + coordinate_data['southwest']['lng']) / 2

    if Location.objects.filter(region=region).exists():
        location = Location.objects.get(region=region)
    else:
        location = Location.objects.create(latitude=latitude, longitude=longitude, country=country, region=region)
    return location


def check_weather(longitude, latitude):
    # url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"  # city
    url = f"http://api.openweathermap.org/data/2.5/weather" \
          f"?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    print(response.__dict__)
