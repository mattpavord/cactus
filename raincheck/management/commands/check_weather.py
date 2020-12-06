from django.core.management.base import BaseCommand


from raincheck.api_tasks import check_location_for_rain
from raincheck.models import Location


class Command(BaseCommand):
    help = 'Makes api call to check weather at specified coordinates'

    def add_arguments(self, parser):
        parser.add_argument('location_id', type=int, help="Id of location to check")

    def handle(self, *args, **options):
        location_id = options['location_id']
        if not Location.objects.filter(id=location_id):
            print("Could not find Location")
            return
        location = Location.objects.get(id=location_id)
        has_rained = check_location_for_rain(location)
        if has_rained:
            print(f"It has rained in {location.region}")
        else:
            print(f"It has not rained in {location.region}")
