import random
import string


class Robot:
    name: str = ""
    usedNames: set = set()
    random.seed(a=None)
    noOfNameLetters: int = 2
    noOfNameNumbers: int = 3

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.name = self.generateName()

    def generateName(self) -> str:
        name: list = []

        while True:
            name.clear()

            for i in range(0, self.noOfNameLetters):
                name.append(random.choice(string.ascii_uppercase))

            for i in range(0, self.noOfNameNumbers):
                name.append(str(random.randrange(0, 9, 1)))

            if ''.join(name) not in self.usedNames:
                break

        name: str = ''.join(name)

        self.usedNames.add(name)
        return name
