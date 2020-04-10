from typing import List
from numbers import Complex

class Matrix:

    def __init__(self, matrix_string: str) -> None:
        self.matrix = self.__string_to_matrix(matrix_string)

    def row(self, index: int) -> List[Complex]:
        return self.matrix[index - 1]

    def column(self, index: int) -> List[Complex]:
        result = []

        for row in self.matrix:
            result.append(row[index - 1])
        return result

    def __string_to_matrix(self, string: str) -> List[Complex]:
        matrix = string.split("\n")

        for row in range(len(matrix)):
            matrix[row] = list(map(complex, matrix[row].split()))

        return matrix