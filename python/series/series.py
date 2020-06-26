def slices(series: str, length: int):
    if length > len(series) or length < 1:
        raise ValueError(
            "Length must be greater than 1 but no longer than the input string")

    result = []
    i = 0
    
    while i+length <= len(series):
        result.append(series[i:i+length])
        i += 1

    return result
