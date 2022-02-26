from django.test import TestCase
from unittest.mock import patch
from interface.management.commands.pop_db import Command as CdeDb
from interface.management.commands.get_picts import Command as CdeP
from interface.management.commands.get_aditional_picts import Command as CdeAP


class Databasetests(TestCase):

    def setUp(self):
        """Instance the class"""

        self.db = CdeDb()
        self.picts = CdeP()
        self.addpicts = CdeAP()

    def mock_handle(self):
        """Setup the handle mock"""

        self.launch_process()

        return "everything is running fine"

    @patch("interface.management.commands.pop_db.Command.handle", mock_handle)
    def test_database_process(self):
        """Lauch the integration test with the two mocks"""

        response = self.db.handle()
        self.assertEqual(response, "everything is running fine")

    @patch("interface.management.commands.get_picts.Command.handle", mock_handle)
    def test_picts_process(self):
        """Lauch the integration test with the two mocks"""

        response = self.picts.handle()
        self.assertEqual(response, "everything is running fine")

    @patch("interface.management.commands.get_aditional_picts.Command.handle", mock_handle)
    def test_addpicts_process(self):
        """Lauch the integration test with the two mocks"""

        response = self.addpicts.handle()
        self.assertEqual(response, "everything is running fine")
