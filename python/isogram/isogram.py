def is_isogram(string: str) -> bool:
    normalized_string = str.lower(str.replace(str.replace(string," ", ""), "-", ""))

    return len(normalized_string) == len(set(normalized_string))
