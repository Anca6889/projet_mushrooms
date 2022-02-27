#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module will get try to get pictures from Wikipedia API using the
scientifist name of mushroom
"""

from django.core.management.base import BaseCommand
from interface.models import Mushroom
import requests
import json


class Command(BaseCommand):
    def launch_process(self):
        """Launch the all process"""

        self.get_pictures_from_wikipedia()

    def get_pictures_from_wikipedia(self):

        for mushroom in Mushroom.objects.all():

            try:

                url = "https://en.wikipedia.org/w/api.php"
                data = {
                    "action": "query",
                    "format": "json",
                    "formatversion": 2,
                    "prop": "pageimages|pageterms",
                    "piprop": "original",
                    "titles": mushroom.espece,
                }
                response = requests.get(url, data)
                json_data = json.loads(response.text)
                image = (
                    json_data["query"]["pages"][0]["original"]["source"]
                    if len(json_data["query"]["pages"]) > 0
                    else "Not found"
                )

                mushroom.image = image
                mushroom.save()

            except ValueError:
                pass

            except KeyError:
                pass

    def handle(self, *args, **options):
        """Alow to use the Django command 'manage.py database'"""

        self.launch_process()
