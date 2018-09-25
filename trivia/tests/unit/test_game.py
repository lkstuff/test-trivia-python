import unittest
from trivia import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def raises_error(*args, **kwds):
        raise ValueError('Invalid value: %s%s' % (args, kwds))

    def test_create_game(self):
        self.assertIsInstance(self.game, Game)
        self.assertListEqual([], self.game.players)


    def test_create_rock_question(self):
        expected = "Rock Question 0"
        self.assertEqual(self.game.create_rock_question(0), expected)

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

    def tearDown(self):
        self.game = None

    if __name__ == '__main__':
        unittest.main()

