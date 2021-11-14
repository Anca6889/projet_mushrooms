from django.test import TestCase
from unittest.mock import patch
from interface.management.commands.pop_db import Command

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
