from bowling_error import BowlingError
from frame import Frame


class BowlingGame:
    frames = []

    def __init__(self):
        pass

    def add_frame(self, frame: Frame) -> None:
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        pass

    def calculate_score(self) -> int:
        pass

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
