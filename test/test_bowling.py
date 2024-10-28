import unittest
import random

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        pass

    def test_game_created(self):
        game = BowlingGame()

        frame = Frame(1, 2)
        game.add_frame(frame)
        self.assertEqual(game.get_frame_at(0), frame)

    def  test_empty_game(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

    def test_game_consists_of_10_frames(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertEqual(len(game._frames), 10)
