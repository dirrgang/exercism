def is_valid(isbn: str) -> bool:
    isbn_list = list(isbn.replace("-", ""))
    if len(isbn_list) != 10:
        return False

    if isbn_list[-1] == "X":
        isbn_list[-1] = 10

    try:
        isbn_list_int = [int(digit) for digit in isbn_list]
    except ValueError:
        return False

    checksum = 0
    for i in range(10):
        checksum += isbn_list_int[i]*(10-i)

    return checksum % 11 == 0
