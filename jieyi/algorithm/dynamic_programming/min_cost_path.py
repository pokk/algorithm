""" Created by Jieyi on 8/18/16. """
from input_data.dynamic_programming.min_cost_path import input_source
from jieyi.algorithm.dynamic_programming import DP


class MCP(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
    """

    def __init__(self, matrix=None):
        self._matrix = matrix
        self._matrix_number_row = len(self._matrix)
        self._matrix_number_col = len(self._matrix[0])
        self._ans_matrix = [[0 for _ in range(self._matrix_number_col)] for _ in range(self._matrix_number_row)]

    def _algorithm(self):
        for i in range(self._matrix_number_col):
            self._ans_matrix[0][i] = self._matrix[0][i] if i == 0 else self._matrix[0][i] + self._ans_matrix[0][i - 1]

        for i in range(self._matrix_number_row):
            self._ans_matrix[i][0] = self._matrix[i][0] if i == 0 else self._matrix[i][0] + self._ans_matrix[i - 1][0]

        for i in range(1, self._matrix_number_col):
            for j in range(1, self._matrix_number_row):
                self._ans_matrix[i][j] = min(self._ans_matrix[i - 1][j - 1], self._ans_matrix[i - 1][j], self._ans_matrix[i][j - 1]) + \
                                         self._matrix[i][j]

    def _backtracking(self):
        pass

    def res(self):
        self._algorithm()
        print(self._ans_matrix[self._matrix_number_row - 1][self._matrix_number_col - 1])


def main():
    for mcp in input_source:
        m = MCP(mcp)
        m.res()


if __name__ == '__main__':
    main()
