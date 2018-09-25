import unittest
from unittest.mock import  patch
import trivia

class TestApp(unittest.TestCase):




    def test_print_in_add_method(self):
        game = trivia.Game()

        with patch('builtins.print') as mocked_print:
            game.add('player_name')
            #mocked_print.assert_called_with('player_name was added')
            mocked_print.assert_called_with('They are player number 1')