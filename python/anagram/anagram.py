from typing import List
from collections import Counter


def find_anagrams(word: str, candidates: List[str]) -> List[str]:

    return [candidate for candidate in candidates if
            is_anagram(word, candidate) and
            word.lower() != candidate.lower()]


def is_anagram(word1: str, word2: str) -> bool:
    return Counter(c for c in word1.lower()) == Counter(c for c in word2.lower())
