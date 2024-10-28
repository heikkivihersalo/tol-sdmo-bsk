import unittest
import random

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def test_game_created(self):
        frame = Frame(1, 2)
        self.game.add_frame(frame)
        self.assertEqual(frame, self.game.get_frame_at(0))

    def test_game_consists_of_10_frames(self):
        for i in range(10):
            first_throw = random.randint(0, 10)
            second_throw = random.randint(0, 10 - first_throw)

            self.game.add_frame(Frame(first_throw, second_throw))

        self.assertEqual(len(self.game._frames), 10)
