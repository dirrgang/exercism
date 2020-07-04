from typing import List, Dict
import re
from collections import Counter


def count_words(sentence: str) -> Dict[str, int]:
    split_sentence: List[str] = re.sub(
        "[!&@$%^&,_]", " ", sentence).lower().split()

    sanitized_sentence = [word.strip(".,'\n: ") for word in split_sentence]

    return Counter(sanitized_sentence)
