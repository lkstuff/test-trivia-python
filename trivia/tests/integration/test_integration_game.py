"""
The trivia.py should be separated
at least an app.py and game.py
according the logic can be more.

This test should check are they working
together properly
"""
import unittest
from trivia import Game


class TestIntegrationGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_create_game(self):
        self.assertIsInstance(self.game, Game)


    def tearDown(self):
        self.game = None
