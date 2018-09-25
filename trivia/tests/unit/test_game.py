from unittest import TestCase
from trivia import Game


class TestGame(TestCase):

    def setUp(self):
        self.game = Game()

    def test_create_game(self):
        self.assertIsInstance(self.game, Game)

    def test_create_rock_question(self):
        pass

    def test_is_playable(self):
        pass

    def test_add(self):
        pass

    def test_how_many_players(self):
        pass

    def test_roll(self):
        pass

    def test_ask_question(self):
        pass

    def test_current_category(self):
        pass

    def test_was_correctly_answered(self):
        pass
    
    def test_wrong_answer(self):
        pass

    def test__did_player_win(self):
        pass
