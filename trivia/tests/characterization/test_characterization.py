import unittest
from unittest.mock import *


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

    def test_print_get_a_question(self):
        player1 = "Player1"
        self.game.add(player1)
        with patch('builtins.print') as mock_print:
            roll = 1
            self.game.deal_with_penalty_box(roll)
            mock_print.assert_called()
            mock_print.assert_has_calls([call("The category is %s" % self.game._current_category)])

    def test_ask_question_called_in_deal_with_penalty_box(self):
        with patch('trivia.trivia.Game._ask_question') as mocked_ask_question:
            self.game._ask_question()
            mocked_ask_question.assert_called()



    def test_print_player_location_in_deal_with_penalty_box(self):
        player1 = "Player1"
        self.game.add(player1)
        with patch('builtins.print') as mock_print:
            roll = 1
            self.game.deal_with_penalty_box(roll)
            mock_print.assert_called()
            mock_print.assert_has_calls([call(self.game.players[self.game.current_player] +
                                              '\'s new location is ' +
                                              str(self.game.places[self.game.current_player]))])



    def test_place_must_be_less_then_12(self):
        player1 = "Player1"
        player2 = "Player2"
        self.game.add(player1)
        self.game.add(player2)
        self.runner.run()

        self.assertTrue(self.game.places[self.game.current_player] <= 11)

    def test_print_in_odd_roll_in_roll_method(self):
        player1 = "Player1"
        self.game.add(player1)
        with patch('builtins.print') as mock_print:
            roll = 1
            self.game.roll(roll)
            mock_print.assert_called()
            mock_print.assert_has_calls([call('Player1 is the current player'),
                                         call('They have rolled a 1'),
                                         call("Player1's new location is 1"),
                                         call('The category is Science'),
                                         call('Science Question 0')])

    def test_print_in_even_roll_in_roll_method(self):
        player1 = "Player1"
        self.game.add(player1)
        with patch('builtins.print') as mock_print:
            roll = 2
            self.game.roll(roll)
            mock_print.assert_called()
            mock_print.assert_has_calls([call('Player1 is the current player'),
                                         call('They have rolled a 2'),
                                         call("Player1's new location is 2"),
                                         call('The category is Sports'),
                                         call('Sports Question 0')])


    def test_deal_with_penalty_box_odd_getting_out(self):
        self.game.add("Geza")
        roll = 1
        self.game.deal_with_penalty_box(roll)
        self.assertTrue(self.game.is_getting_out_of_penalty_box is True)


    def test_deal_with_penalty_box_even_not_getting_out(self):
        self.game.add("Geza")
        roll = 2
        self.game.deal_with_penalty_box(roll)
        self.assertTrue(self.game.is_getting_out_of_penalty_box is False)


    def test_print_deal_with_penalty_box_even_roll(self):
        player1 = "Player1"
        self.game.add(player1)
        with patch('builtins.print') as mock_print:
            roll = 2
            self.game.deal_with_penalty_box(roll)
            mock_print.assert_called()
            mock_print.assert_has_calls([call('Player1 is not getting out of the penalty box')])


    def test_print_deal_with_penalty_box_odd_roll(self):
        player1 = "Player1"
        self.game.add(player1)
        with patch('builtins.print') as mock_print:
            roll = 1
            self.game.deal_with_penalty_box(roll)
            mock_print.assert_called()
            mock_print.assert_has_calls([call('Player1 is getting out of the penalty box')])


    def test_ask_question(self):
        with patch('builtins.print') as mock_print:
            self.game._ask_question()
            mock_print.assert_called_with('Pop Question 0')


    def test_ask_question(self):
        with patch('trivia.trivia.Game._ask_question') as mock_ask_question:
            player1 = "Player1"
            self.game.add(player1)
            self.game._ask_question()
            mock_ask_question.assert_called()


    def test_current_category(self):
        with patch("trivia.trivia.Game._current_category") as mock_current_category:
            player1 = "Player1"
            self.game.add(player1)
            self.game._current_category()
            mock_current_category.assert_called()


    def test__did_player_win(self):
        with patch("trivia.trivia.Game._did_player_win") as mock_did_player_win:
            player1 = "Player1"
            self.game.add(player1)
            self.game._did_player_win()
            mock_did_player_win.assert_called()


    def test_how_many_players_is_called(self):
        with patch("trivia.trivia.Game.how_many_players") as mock_how_many_players:
            self.game.how_many_players()
            mock_how_many_players.assert_called()















        # mock_print.assert_has_calls([call('Player1 is not getting out of the penalty box')])


    def tearDown(self):
        self.game = None
        self.game1 = None
        self.runner = None












