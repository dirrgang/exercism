def latest(scores: list) -> int:
    return scores[-1]


def personal_best(scores: list) -> int:
    result: list = scores
    result.sort()
    return result[-1]


def personal_top_three(scores: list) -> list:
    result: list = scores
    result.sort()
    return result[-3::][::-1]
