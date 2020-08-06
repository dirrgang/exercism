import string


def is_pangram(sentence: str):
    # A pangram (Greek: παν γράμμα, pan gramma, "every letter")
    # is a sentence using every letter of the alphabet at least once.
    for letter in string.ascii_lowercase:
        if string.punctuation.find(letter) >= 0:
            continue
        elif sentence.lower().find(letter) < 0:
            return False
    return True
