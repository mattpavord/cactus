import requests
from typing import List, Optional

from bs4 import BeautifulSoup
from django.db import transaction

from raincheck.models import Plant, Location


def get_soup(url: str) -> BeautifulSoup:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    return BeautifulSoup(page.content, 'html.parser')


def get_location_data_from_str(location_text: str) -> dict:
    continent = location_text[location_text.find("(") + 1:location_text.find(")")]
    if ',' in continent:
        continent = continent.split(',')[-1]

    if ':' in location_text:
        location_text = location_text.split(':')[-1]

    if ' - ' in location_text:
        country = location_text.split(' - ')[1].split('(')[0]
        local = location_text.split(' - ')[0]
        if ',' in local:
            local = local.split(',')[-1]
    else:
        country = location_text.split('(')[0]
        local = country

    location = {
        'continent': continent.strip(),
        'country': country.strip(),
        'local': local.strip(),
    }
    return location


def get_cacti_names(letter) -> List[str]:
    """ Queries cactiguide.come for cacti names """
    url = f'https://cactiguide.com/name_search/?initial={letter}'
    soup = get_soup(url)
    table = soup.find_all('table')[-1]
    rows = table.find_all('tr')
    cacti_names = []
    for row in rows:
        cactus_name = row.text.replace('\n', '')
        cacti_names.append(cactus_name)
    return cacti_names


def get_location(cactus_name: str) -> Optional[dict]:
    cactus_name = cactus_name.replace(' ', '%20')
    url = f"https://cactiguide.com/cactus/?uname={cactus_name}"
    soup = get_soup(url)
    text = soup.get_text().split('\n')
    for row in text:
        if "Distribution" in row:
            location_text = row[14:]
            try:
                return get_location_data_from_str(location_text)
            except IndexError:
                print("Error: " + location_text)
    return None


def main():
    plants = []
    cacti_names = get_cacti_names('N')
    for cactus in cacti_names:
        location = get_location(cactus)
        if location and location.get('local'):
            if not Location.objects.filter(region=location['local']).exists():
                location_obj = Location.objects.create(
                    region=location['local'],
                    country=location['country'],
                    continent=location['continent'],
                )
            else:
                location_obj = Location.objects.get(region=location['local'])
            if not Plant.objects.filter(name=cactus).exists():
                plant = Plant(location_id=location_obj.id, name=cactus, reference="cactiguide.com")
                plants.append(plant)
                print(cactus, plant.location_id)
    Plant.objects.bulk_create(plants)
