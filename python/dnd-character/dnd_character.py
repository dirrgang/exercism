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
        # These six abilities have scores that are determined randomly. You do this
        # by rolling four 6-sided dice and record the sum of the largest three dice.
        # You do this six times, once for each ability.
        return sum(sorted(random.sample(range(1, 6), 4))[1:])


def modifier(ability: int) -> int:
    # Your character's initial hitpoints are 10 + your character's constitution
    # modifier. You find your character's constitution modifier by subtracting
    # 10 from your character's constitution, divide by 2 and round down.
    return floor((ability - 10) / 2)
