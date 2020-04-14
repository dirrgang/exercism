import random
from typing import List

class Character:
    strength: List[int] = [0, 0]
    dexterity: List[int] = [0, 0]
    constitution: List[int] = [0, 0]
    intelligence: List[int] = [0, 0]
    wisdom: List[int] = [0, 0]
    charisma: List[int] = [0, 0]
    stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]

    hitpoints: int = 0


    def __init__(self) -> None:
        for ability in self.stats:
            ability[0] = sum(sorted(random.sample(range(1, 6), 5))[2:])
            print(ability)
        return
        
def modifier(ability) -> int:

    
    return 0