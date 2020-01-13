import pytest, unittest
from application import app, routes
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app

class TestApp(TestBase):
    #testing the connection
    def test_card_page(self):
        response = self.client.get(url_for('crystals'))
        self.assertEqual(response.status_code, 200)

    #testing the card generator
    def test_crystal_generator(self):
        listOfCrystals = ["Dolomite", "Blue Opal", "Astrophyllite" , "Azurite" , "Tiger's Eye", "Blue Lace"]
        crystal  = routes.crystal_generator()
        self.assertIn(crystal)
