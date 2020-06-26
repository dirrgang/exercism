from typing import List


class Matrix:

    def __init__(self, matrix_string: str) -> None:
        self.matrix = self._string_to_matrix(matrix_string)

    def row(self, index: int) -> List[complex]:
        return self.matrix[index-1]

    def column(self, index: int) -> List[complex]:
        return [row[index-1] for row in self.matrix]

    def _string_to_matrix(self, string: str) -> List[List[complex]]:
        return [list(map(complex, row.split())) for row in string.split("\n")]
