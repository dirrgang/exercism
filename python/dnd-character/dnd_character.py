import random
from math import floor


class Character:
    def __init__(self) -> None:
        self.strength: int = self.ability()
        self.dexterity: int = self.ability()
        self.constitution: int = self.ability()
        self.intelligence: int = self.ability()
        self.wisdom: int = self.ability()
        self.charisma: int = self.ability()
        self.hitpoints: int = 10 + modifier(self.constitution)

    def ability(self) -> int:
        return sum(sorted(random.sample(range(1, 6), 4))[1:])


def modifier(ability: int) -> int:
    return floor((ability - 10) / 2)
