import unittest
from unittest.mock import patch

from trivia.trivia import *


class TestCharacterization(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game1 = Game(autorun=False)
        self.runner = Runner(self.game)

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

    def test_game_initialization_pop_questions_empty(self):
        self.assertEqual(len(self.game1.pop_questions), 0)

    def test_game_initialization_science_questions_empty(self):
        self.assertEqual(len(self.game1.science_questions), 0)

    def test_game_initialization_sports_questions_empty(self):
        self.assertEqual(len(self.game1.sports_questions), 0)

    def test_game_initialization_rock_questions_empty(self):
        self.assertEqual(len(self.game1.rock_questions), 0)

    def test_game_initialization_current_player_is_null(self):
        self.assertEqual(self.game.current_player, 0)

    def test_game_initialization_is_getting_out_of_penalty_box_is_false(self):
        self.assertFalse(self.game.is_getting_out_of_penalty_box)

    def test_game_initialization_is_questions_filled_up(self):
        self.assertEqual(len(self.game.rock_questions), 50)
        self.assertEqual(len(self.game.sports_questions), 50)
        self.assertEqual(len(self.game.science_questions), 50)
        self.assertEqual(len(self.game.pop_questions), 50)

    def test_create_rock_question(self):
        index = randrange(50)
        expected = "Rock Question %s" % index
        self.assertEqual(self.game.create_rock_question(index), expected)

    def test_how_many_players(self):
        expected = len(self.game.players)
        self.assertEqual(self.game.how_many_players, expected)

    def test_is_playable(self):
        self.assertFalse(self.game.how_many_players >= 2)
        self.game.add("Player1", autorun=False)
        self.assertFalse(self.game.how_many_players >= 2)
        self.game.add("Player2", autorun=False)
        self.assertTrue(self.game.how_many_players >= 2)

    def test_add_return_True(self):
        name = "Player1"
        self.assertTrue(self.game.add(name))

    def test_add_player_to_players(self):
        name = "Player1"
        expected = len(self.game.players) + 1
        self.game.add(name, autorun=False)
        self.assertEqual(len(self.game.players), expected)

    def test_add_starting_player_location_is_0(self):
        name = "Player1"
        self.game.add(name, autorun=False)
        self.assertEqual(self.game.places[self.game.how_many_players], 0)

    def test_add_starting_player_has_no_coin(self):
        name = "Player1"
        self.game.add(name, autorun=False)
        self.assertEqual(self.game.purses[self.game.how_many_players], 0)

    def test_add_starting_player_not_in_penalty_box(self):
        name = "Player1"
        self.game.add(name, autorun=False)
        self.assertFalse(self.game.in_penalty_box[self.game.how_many_players])

    def test_print_added_player_and_number(self):
        with patch('builtins.print') as mocked_print:
            name = "Player1"
            self.game.print_added_player_and_number(name)
            mocked_print.side_effect = (name + " was added", "They are player number %s" % len(self.game.players))
            mocked_print.assert_called()

    @unittest.skip("no get question")
    def test_print_get_a_question(self):
        with patch('builtins.print') as mocked_print:
            self.game.get_a_question()
            mocked_print.assert_called()

    def test_ask_question_called_in_get_question(self):
        with patch('trivia.trivia.Game._ask_question') as mocked_ask_question:
            self.game._ask_question()
            mocked_ask_question.assert_called()
    @unittest.skip("no attribute player location")
    def test_print_player_location(self):
        with patch('builtins.print') as mocked_print:
            player = "Player1"
            self.game.add(player)
            self.game.print_player_location()
            mocked_print.assert_called()

    def test_place_must_be_less_then_12(self):
        player1 = "Player1"
        player2 = "Player2"
        self.game.add(player1)
        self.game.add(player2)
        self.runner.run()

        self.assertTrue(self.game.places[self.game.current_player] <= 11)

    @unittest.skip("Penalty  logic")
    def test_print_deal_with_penalty_box_even_roll(self):
        with patch('builtins.print') as mocked_print:
            self.game.add("Geza")
            roll = 2
            self.game.roll(roll)

            mocked_print.assert_called_with('Geza is not getting out of the penalty box')


    @unittest.skip("With odd numbers calls the print method from the ask_question method")
    def test_print_deal_with_penalty_box_odd_roll(self):
        with patch('builtins.print') as mocked_print:
            self.game.add("Geza")

            self.game.deal_with_penalty_box(3)

            mocked_print.assert_called_with('Geza is getting out of the penalty box')













    def tearDown(self):
        self.game = None
        self.game1 = None
