from typing import List
import re


def abbreviate(words: str) -> str:

    # Replaces various unwanted characters with a space, turns the string uppercase and
    # then splits the string into a List of strings, removing all spaces inbetween.
    sanitized_words: List[str] = (
        re.sub("[!&@$%^&,_-]", " ", words.upper())).split()

    # Takes the first letter of every string element in the list and joins them into a string
    return ''.join([word[0] for word in sanitized_words])
