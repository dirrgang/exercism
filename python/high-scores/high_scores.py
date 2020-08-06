from typing import List

def latest(scores: List[int]) -> int:
    return scores[-1]


def personal_best(scores: List[int]) -> int:
    result: List[int] = scores
    result.sort()
    return result[-1]


def personal_top_three(scores: List[int]) -> List[int]:
    result: List[int] = scores
    result.sort()
    return result[-3::][::-1]
