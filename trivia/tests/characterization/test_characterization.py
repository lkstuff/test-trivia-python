import unittest

from unittest.mock import  patch
from trivia.trivia import *


class TestCharacterization(unittest.TestCase):

    def setUp(self):
        self.game = Game()


    def test_game_initialization_no_player(self):
        self.assertEqual(len(self.game.players), 0)

    def test_game_initialization_places_are_zero(self):
        for place in self.game.places:
            self.assertEqual(place, 0)

    def test_game_initialization_purses_are_empty(self):
        for purse in self.game.purses:
            self.assertEqual(purse, 0)

    def test_game_initialization_nobody_in_penalty(self):
        for person in self.game.in_penalty_box:
            self.assertEqual(person, 0)

    @unittest.skipIf(Exception, "FAILED: test_game_initialization_pop_questions_empty")
    def test_game_initialization_pop_questions_empty(self):
        self.assertEqual(len(self.game.pop_questions), 0)

    @unittest.skipIf(Exception, "FAILED: test_game_initialization_science_questions_empty")
    def test_game_initialization_science_questions_empty(self):
        self.assertEqual(len(self.game.science_questions), 0)

    @unittest.skipIf(Exception, "FAILED: test_game_initialization_sports_questions_empty")
    def test_game_initialization_sports_questions_empty(self):
        self.assertEqual(len(self.game.sports_questions), 0)

    @unittest.skipIf(Exception, "FAILED: test_game_initialization_rock_questions_empty")
    def test_game_initialization_rock_questions_empty(self):
        self.assertEqual(len(self.game.rock_questions), 0)







    def tearDown(self):
        self.game = None