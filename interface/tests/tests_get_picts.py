from django.test import TestCase
from unittest.mock import patch
from interface.models import Mushroom
from interface.management.commands.get_picts import Command


class Databasetests(TestCase):

    def setUp(self):
        """Instance the class"""

        self.db = Command()

    def mock_handle(self):
        """Setup the handle mock"""

        self.launch_process()
        return "everything is running fine"

    @patch("interface.management.commands.pop_db.Command.handle", mock_handle)
    def test_database_process(self):
        """Lauch the integration test with the two mocks"""

        response = self.db.handle()
        self.assertEqual(response, "everything is running fine")

    def mock_request_api(self):
        """Setup the API request method mock with fake results"""

        for mushroom in Mushroom.objects.all():
            mock_results = [
                [
                    {
                        "image": "image",
                    },
                ],
            ]
            mushroom.image = mock_results
            mushroom.save()

    @patch("interface.management.commands.get_picts.Command.handle", mock_handle)
    @patch("interface.management.commands.get_picts.Command.get_pictures_from_wikipedia",
           mock_request_api)
    def test_database_process(self):
        """Lauch the integration test with the two mocks"""

        response = self.db.handle()
        self.assertEqual(response, "everything is running fine")
