from typing import List


class Matrix:

    def __init__(self, matrix_string: str) -> None:
        self.matrix = self._string_to_matrix(matrix_string)

    def row(self, index: int) -> List[complex]:
        return self.matrix[index - 1]

    def column(self, index: int) -> List[complex]:
        column: List[complex] = []

        for row in self.matrix:
            column.append(row[index - 1])
        return column

    def _string_to_matrix(self, string: str) -> List[List[complex]]:
        rows = string.split("\n")

        matrix: List[List[complex]] = []

        for row in range(len(rows)):
            matrix.append(list(map(complex, rows[row].split())))

        return matrix
