import json
import requests
from django.conf import settings

from raincheck.models import Location

WEATHER_API_KEY = settings.WEATHER_API_KEY
GOOGLE_API_KEY = settings.GOOGLE_API_KEY


def get_or_create_location_from_google_api(location_str: str) -> Location:
    """
    Makes an api request to google geocoder to clean data and create a location object
    This will:
     - Add/clean the country
     - Add the coordinates
     - Not create duplicate locations based on region (administrative_area_level_1) according to google
    """
    url = f'https://maps.googleapis.com/maps/api/geocode/' \
          f'json?address={location_str}&key={GOOGLE_API_KEY}'
    response = requests.get(url)
    if response.status_code != 200:
        raise NameError(response.content)

    data = json.loads(response.content)['results'][0]

    country = ''
    region = location_str
    for address_component in data['address_components']:
        if 'administrative_area_level_1' in address_component['types']:
            region = address_component['long_name']
        if 'country' in address_component['types']:
            country = address_component['long_name']
    latitude = data['geometry']['location']['lat']
    longitude = data['geometry']['location']['lng']

    if Location.objects.filter(region=region).exists():
        location = Location.objects.get(region=region)
    else:
        location = Location.objects.create(latitude=latitude, longitude=longitude, country=country, region=region)
    return location


def check_location_for_rain(location: Location) -> bool:
    """
    Makes an api request to openweathermap to check a location for weather,
    does this by using longitude and latitude parameters of location
    Returns boolean on whether it has rained or not
    """
    url = f"http://api.openweathermap.org/data/2.5/weather" \
          f"?lat={location.latitude}&lon={location.longitude}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        raise NameError(response.content)
    data = json.loads(response.content)
    return 'rain' in data
