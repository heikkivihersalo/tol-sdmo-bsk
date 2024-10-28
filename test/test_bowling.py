import unittest
import random

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.default_game = BowlingGame()

        self.default_game.add_frame(Frame(1, 5))
        self.default_game.add_frame(Frame(3, 6))
        self.default_game.add_frame(Frame(7, 2))
        self.default_game.add_frame(Frame(3, 6))
        self.default_game.add_frame(Frame(4, 4))
        self.default_game.add_frame(Frame(5, 3))
        self.default_game.add_frame(Frame(3, 3))
        self.default_game.add_frame(Frame(4, 5))
        self.default_game.add_frame(Frame(8, 1))
        self.default_game.add_frame(Frame(2, 6))

    def test_game_created(self):
        special_game = BowlingGame()

        frame = Frame(1, 2)
        special_game.add_frame(frame)
        self.assertEqual(special_game.get_frame_at(0), frame)

    def  test_empty_game(self):
        special_game = BowlingGame()
        self.assertRaises(BowlingError, special_game.get_frame_at, 0)

    def test_game_created_10_frames(self):
        self.assertEqual(len(self.default_game._frames), 10)

    def test_game_created_11_frames(self):
        self.assertRaises(BowlingError, self.default_game.add_frame, Frame(3, 6))

    def test_game_index_negative(self):
        self.assertRaises(BowlingError, self.default_game.get_frame_at, -1)

    def test_game_index_out_of_bounds(self):
        self.assertRaises(BowlingError, self.default_game.get_frame_at, 11)

    def test_calculate_score(self):
        self.assertEqual(self.default_game.calculate_score(), 81)

    def test_calculate_score_spare(self):
        self.special_game = BowlingGame()

        self.special_game.add_frame(Frame(1, 9))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(7, 2))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(4, 4))
        self.special_game.add_frame(Frame(5, 3))
        self.special_game.add_frame(Frame(3, 3))
        self.special_game.add_frame(Frame(4, 5))
        self.special_game.add_frame(Frame(8, 1))
        self.special_game.add_frame(Frame(2, 6))

        self.assertEqual(self.special_game.calculate_score(), 88)
