# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:

    def __init__(self, word: str):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = list(word)
        self.masked_word = list("_"*len(word))

    def guess(self, char: str) -> str:
        if not self.status == STATUS_ONGOING:
            raise ValueError(char)

        changed = False

        for i in range(len(self.word)):
            if self.word[i] == char and self.word[i] != self.masked_word[i]:
                changed = True
                self.masked_word[i] = self.word[i]

        if changed == False:
            self.remaining_guesses -= 1

        if self.masked_word == self.word:
            self.status = STATUS_WIN

        elif self.remaining_guesses == -1:
            self.status = STATUS_LOSE

    def get_masked_word(self) -> str:
        return "".join(self.masked_word)

    def get_status(self) -> str:
        return self.status
