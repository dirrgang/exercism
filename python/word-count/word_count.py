from typing import List, Dict
import re
from collections import Counter


def count_words(sentence: str) -> Dict[str, int]:

    # Uses regular expressions to replace various unwanted characters and replaces them
    # with spaces. Using spaces instead of removing them entirely allows for split() to
    # match words properly. lower() for consistency. Note that punctuation is not removed
    # at this point, as not to remove certain characters within words.
    split_sentence: List[str] = re.sub(
        "[!&@$%^&,_]", " ", sentence).lower().split()

    # Strips punctuation left and right from the word and turns it into a list
    sanitized_sentence: List[str] = [
        word.strip(".,'\n: ") for word in split_sentence]

    # Counter counts the number of times an item appears in a list and returns a dict
    return Counter(sanitized_sentence)
