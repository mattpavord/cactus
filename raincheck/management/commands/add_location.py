from django.core.management.base import BaseCommand


from raincheck.api_tasks import get_or_create_location_from_google_api


class Command(BaseCommand):
    help = 'Makes api call to check weather at specified coordinates'

    def add_arguments(self, parser):
        parser.add_argument('location_str', type=str, help="Location to add")

    def handle(self, *args, **options):
        location_str = options['location_str']
        get_or_create_location_from_google_api(location_str)
