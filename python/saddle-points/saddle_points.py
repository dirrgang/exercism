from typing import List


def saddle_points(matrix: List[List[int]]) -> List[int]:
    saddles = []

    def return_row(matrix: List[List[int]], index: int) -> List[int]:
        return matrix[index]

    def return_column(matrix: List[List[int]], index: int) -> List[int]:
        return [row[index] for row in matrix]

    def verify_matrix(matrix: List[List[int]]) -> None:
        if len(matrix) != 0:
            for row in matrix:
                if len(row) != len(matrix[0]):
                    raise ValueError("Malformed Matrix!")

    verify_matrix(matrix)

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == max(return_row(matrix, x)) and matrix[x][y] == min(return_column(matrix, y)):
                saddles.append({"row": x+1, "column": y+1})

    return saddles
