def rotate(text: str, key: int):
    result: list[str] = ""

    for letter in text:
        letterNum: int = ord(letter)
        if letter.islower():
            result += chr(((letterNum - ord("a") + key) % 26) + ord("a"))
        elif letter.isupper():
            result += chr(((letterNum - ord("A") + key) % 26) + ord("A"))
        else:
            result += letter

    return result
