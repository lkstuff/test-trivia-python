import unittest
from unittest.mock import  patch
from trivia.trivia import *


class TestCharacterization(unittest.TestCase):

    def setUp(self):
        self.game = Game()


    def tearDown(self):
        self.game = None