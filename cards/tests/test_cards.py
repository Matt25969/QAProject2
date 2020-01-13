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
        response = self.client.get(url_for('cards'))
        self.assertEqual(response.status_code, 200)
    
    #testing the card generator
    def test card_generator(self):
        cards_names = ["The Fool",
            "The Magician",
            "The High Priestess",
            "The Empress",
            "The Emperor",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgement",
            "The World"]
        card  = routes.shufflecards()
        self.assertIn(card)
