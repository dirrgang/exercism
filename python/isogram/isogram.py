def is_isogram(string: str) -> bool:
    normalized_string = string.lower().replace(" ", "").replace("-", "")

    return len(normalized_string) == len(set(normalized_string))
