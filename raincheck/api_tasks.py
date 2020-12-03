from typing import Tuple
import json
import requests
from django.conf import settings

from raincheck.models import Location

WEATHER_API_KEY = settings.WEATHER_API_KEY
GOOGLE_API_KEY = settings.GOOGLE_API_KEY


def add_coordinate_to_location(location: Location):
    location_str = location.region
    if location.country:
        location_str = ', '.join([location.region, location.country])
    longitude, latitude = get_coordinates_from_location(location_str)
    location.longitude = longitude
    location.latitude = latitude
    location.save()


def get_coordinates_from_location(place: str) -> Tuple[float, float]:
    url = f'https://maps.googleapis.com/maps/api/geocode/' \
          f'json?address={place}&key={GOOGLE_API_KEY}'
    response = requests.get(url)
    data = json.loads(response.content)
    coordinate_data = data['results'][0]['geometry']['bounds']
    latitude = (coordinate_data['northeast']['lat'] + coordinate_data['southwest']['lat']) / 2
    longitude = (coordinate_data['northeast']['lng'] + coordinate_data['southwest']['lng']) / 2
    return latitude, longitude


def check_weather(longitude, latitude):
    # url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"  # city
    url = f"http://api.openweathermap.org/data/2.5/weather" \
          f"?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    print(response.__dict__)


if __name__ == '__main__':
    print(get_coordinates_from_location('Woodhouse Eaves, Leicester'))
    # check_weather()
