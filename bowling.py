from bowling_error import BowlingError
from frame import Frame
import random


class BowlingGame:
    def __init__(self):
        self._frames = []

    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) == 10:
            raise BowlingError("Game is full")
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if len(self._frames) == 0:
            raise BowlingError("Game is empty")

        if i < 0:
            raise BowlingError("Frame index out of bounds")

        if i >= len(self._frames):
            raise BowlingError("Frame index out of bounds")

        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
        for i in self._frames:
            score += i.score()

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
