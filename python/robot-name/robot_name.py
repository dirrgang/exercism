import random
import string
from typing import List


class Robot:
    name: str = ""
    usedNames: set[str] = set()
    random.seed(a=None)
    noOfNameLetters: int = 2
    noOfNameNumbers: int = 3

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.name = self.generateName()

    def generateName(self) -> str:
        nameList: List[str] = []

        while True:
            nameList.clear()

            for i in range(0, self.noOfNameLetters):
                nameList.append(random.choice(string.ascii_uppercase))

            for i in range(0, self.noOfNameNumbers):
                nameList.append(str(random.randrange(0, 9, 1)))

            if ''.join(nameList) not in self.usedNames:
                break

        result: str = ''.join(nameList)

        self.usedNames.add(result)
        return result
