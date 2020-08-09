from django.core.management.base import BaseCommand, CommandError

from raincheck import scraper_tasks


class Command(BaseCommand):
    help = 'Scrapes cactiguide for cacti names and locations'

    def handle(self, *args, **options):
        scraper_tasks.main()
