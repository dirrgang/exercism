def score(word: str) -> int:
    letter_values: dict[str, int] = {}
    letter_values.update(dict.fromkeys(
        ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 1))
    letter_values.update(dict.fromkeys(["D", "G"], 2))
    letter_values.update(dict.fromkeys(["B", "C", "M", "P"], 3))
    letter_values.update(dict.fromkeys(["F", "H", "V", "W", "Y"], 4))
    letter_values.update(dict.fromkeys(["K"], 5))
    letter_values.update(dict.fromkeys(["J", "X"], 8))
    letter_values.update(dict.fromkeys(["Q", "Z"], 10))

    return sum([letter_values.get(letter, 0) for letter in str.upper(word)])
