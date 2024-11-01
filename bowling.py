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
        is_perfect_game = True

        for index, frame in enumerate(self._frames):
            # Keep track of perfect game
            if not frame.is_strike():
                is_perfect_game = False

            # Handle base score
            score += frame.score()

            # Handle spare
            if frame.is_spare():
                if index == 9:
                    continue

                next_frame = self.get_frame_at(index + 1)
                score += next_frame.get_first_throw()

            # Handle strike
            if frame.is_strike():
                if index == 9:
                    continue

                next_frame = self.get_frame_at(index + 1)
                score += next_frame.score()

                if next_frame.is_strike():
                    if index == 8 or index == 9:
                        continue

                    next_2_frame = self.get_frame_at(index + 2)
                    score += next_2_frame.get_first_throw()

        # If all frames are strikes then the score is 300
        if is_perfect_game:
            return 300

        # All other cases
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self._frames[-1].set_bonus(bonus_throw)

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self._frames[-1].set_bonus(bonus_throw)
