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
        self.assertEqual(10, len(self.default_game._frames))

    def test_game_created_11_frames(self):
        self.assertRaises(BowlingError, self.default_game.add_frame, Frame(3, 6))

    def test_game_index_negative(self):
        self.assertRaises(BowlingError, self.default_game.get_frame_at, -1)

    def test_game_index_out_of_bounds(self):
        self.assertRaises(BowlingError, self.default_game.get_frame_at, 11)

    def test_calculate_score(self):
        self.assertEqual(81, self.default_game.calculate_score())

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

        self.assertEqual(88, self.special_game.calculate_score())

    def test_calculate_score_strike(self):
        self.special_game = BowlingGame()

        self.special_game.add_frame(Frame(10, 0))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(7, 2))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(4, 4))
        self.special_game.add_frame(Frame(5, 3))
        self.special_game.add_frame(Frame(3, 3))
        self.special_game.add_frame(Frame(4, 5))
        self.special_game.add_frame(Frame(8, 1))
        self.special_game.add_frame(Frame(2, 6))

        self.assertEqual(94, self.special_game.calculate_score())

    def test_calculate_score_strike_followed_by_spare(self):
        self.special_game = BowlingGame()

        self.special_game.add_frame(Frame(10, 0))
        self.special_game.add_frame(Frame(4, 6))
        self.special_game.add_frame(Frame(7, 2))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(4, 4))
        self.special_game.add_frame(Frame(5, 3))
        self.special_game.add_frame(Frame(3, 3))
        self.special_game.add_frame(Frame(4, 5))
        self.special_game.add_frame(Frame(8, 1))
        self.special_game.add_frame(Frame(2, 6))

        self.assertEqual(103, self.special_game.calculate_score())

    def test_calculate_score_strike_followed_by_strike(self):
        self.special_game = BowlingGame()

        self.special_game.add_frame(Frame(10, 0))
        self.special_game.add_frame(Frame(10, 0))
        self.special_game.add_frame(Frame(7, 2))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(4, 4))
        self.special_game.add_frame(Frame(5, 3))
        self.special_game.add_frame(Frame(3, 3))
        self.special_game.add_frame(Frame(4, 5))
        self.special_game.add_frame(Frame(8, 1))
        self.special_game.add_frame(Frame(2, 6))

        self.assertEqual(112, self.special_game.calculate_score())

    def test_calculate_score_spare_followed_by_spare(self):
        self.special_game = BowlingGame()

        self.special_game.add_frame(Frame(8, 2))
        self.special_game.add_frame(Frame(5, 5))
        self.special_game.add_frame(Frame(7, 2))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(4, 4))
        self.special_game.add_frame(Frame(5, 3))
        self.special_game.add_frame(Frame(3, 3))
        self.special_game.add_frame(Frame(4, 5))
        self.special_game.add_frame(Frame(8, 1))
        self.special_game.add_frame(Frame(2, 6))

        self.assertEqual(98, self.special_game.calculate_score())

    def test_calculate_score_spare_as_last_frame(self):
        self.special_game = BowlingGame()

        self.special_game.add_frame(Frame(1, 5))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(7, 2))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(4, 4))
        self.special_game.add_frame(Frame(5, 3))
        self.special_game.add_frame(Frame(3, 3))
        self.special_game.add_frame(Frame(4, 5))
        self.special_game.add_frame(Frame(8, 1))
        self.special_game.add_frame(Frame(2, 8))

        self.special_game.set_first_bonus_throw(7)

        self.assertEqual(90, self.special_game.calculate_score())

    def test_calculate_score_strike_as_last_frame(self):
        self.special_game = BowlingGame()

        self.special_game.add_frame(Frame(1, 5))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(7, 2))
        self.special_game.add_frame(Frame(3, 6))
        self.special_game.add_frame(Frame(4, 4))
        self.special_game.add_frame(Frame(5, 3))
        self.special_game.add_frame(Frame(3, 3))
        self.special_game.add_frame(Frame(4, 5))
        self.special_game.add_frame(Frame(8, 1))
        self.special_game.add_frame(Frame(10, 0))

        self.special_game.set_first_bonus_throw(7)
        self.special_game.set_second_bonus_throw(2)

        self.assertEqual(92, self.special_game.calculate_score())

