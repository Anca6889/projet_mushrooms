from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError
from interface.models import Mushroom
from progress.bar import FillingSquaresBar
import requests
import json


class Command(BaseCommand):

    def launch_process(self):
        """Launch the all process"""

        self.get_pictures_from_wikipedia()

    def get_pictures_from_wikipedia(self):

        for mushroom in Mushroom.objects.filter(image__isnull=True):
            
            try:

                url = 'https://fr.wikipedia.org/w/api.php'
                data = {
                    'action': 'query',
                    'format': 'json',
                    'formatversion': 2,
                    'prop': 'pageimages|pageterms',
                    'piprop': 'original',
                    'titles': mushroom.nom_vernaculaire
                }
                response = requests.get(url, data)
                json_data = json.loads(response.text)
                image = (json_data['query']['pages'][0]['original']['source'] if len(
                    json_data['query']['pages']) > 0 else 'Not found')

                mushroom.image = image
                mushroom.save()

            except ValueError:
                pass

            except KeyError:
                pass

    def handle(self, *args, **options):
        """Alow to use the Django command 'manage.py database'"""

        self.launch_process()
