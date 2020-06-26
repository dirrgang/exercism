from typing import List

def value(colors: List[str]) -> int:
    color_dict = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }

    digits = [color_dict.get(str.lower(key), -1) for key in colors[0:2]]

    return int(''.join(map(str, digits)))