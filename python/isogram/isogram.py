def is_isogram(string: str) -> bool:
    normalized_string: str = string.lower().replace(" ", "").replace("-", "")

    # Using a set to remove any duplicate letters - if the length is then
    # unequal to the length of the string, there was a duplicate.
    return len(normalized_string) == len(set(normalized_string))
