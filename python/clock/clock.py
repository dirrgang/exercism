from __future__ import annotations
from math import floor


class Clock:
    hour: int = 0
    minute: int = 0

    def __init__(self, hour: int, minute: int) -> None:

        # To handle inits with minutes > 60, we need to calculate the appropriate
        # number of hours and add it to self.hour instead.
        self.hour = (hour + floor((minute / 60))) % 24
        self.minute = minute % 60

    def __repr__(self) -> str:
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other: Clock) -> bool:
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> Clock:
        # Convert minutes to hours in case of minutes >= 60
        self.hour = (self.hour + floor((self.minute + minutes) / 60)) % 24
        self.minute = (self.minute + minutes) % 60
        return self

    def __sub__(self, minutes: int) -> Clock:
        # Substract minutes from hours in case of minutes >= 60
        self.hour = (self.hour + floor((self.minute - minutes) / 60)) % 24
        self.minute = (self.minute - minutes) % 60
        return self
