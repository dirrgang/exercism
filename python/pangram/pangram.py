def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "._-\"\'"

    for letter in alphabet:
        if punctuation.find(letter) >= 0:
            continue
        elif sentence.lower().find(letter) < 0:
            return False
    return True
