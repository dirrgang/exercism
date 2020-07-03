from __future__ import annotations
from math import floor


class Clock:
    hour: int = 0
    minute: int = 0

    def __init__(self, hour: int, minute: int) -> None:
        self.hour = (hour + floor((minute / 60))) % 24
        self.minute = minute % 60

    def __repr__(self) -> str:
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other: Clock) -> bool:
        return self.hour % 24 == other.hour % 24 and self.minute % 60 == other.minute % 60

    def __add__(self, minutes: int) -> Clock:
        self.hour = (self.hour + floor((self.minute + minutes) / 60)) % 24
        self.minute = (self.minute + minutes) % 60
        return self

    def __sub__(self, minutes: int) -> Clock:
        self.hour = (self.hour + floor((self.minute - minutes) / 60)) % 24
        self.minute = (self.minute - minutes) % 60
        return self
