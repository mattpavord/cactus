from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Scrapes cactiguide for cacti names and locations'

    def handle(self, *args, **options):
        pass