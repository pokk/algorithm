""" Created by Jieyi on 8/25/16. """
import sys

from input_data.dynamic_programming.matrix_chain_multiplication import input_source
from jieyi.algorithm.dynamic_programming import DP


class MCM(DP):
    """
    Matrix Chain Multiplication algorithm as belong Dynamic Programming.
    The problem's url is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    """

    def __init__(self, matrix):
        self._matrix_arr = matrix
        self._res_matrix = [[0 for _ in range(len(self._matrix_arr))] for _ in range(len(self._matrix_arr))]

    def _preset(self):
        pass

    def _algorithm(self):
        i, j, loop_count = 1, 1, 1
        while True:
            if i == 1 and j == len(self._matrix_arr):
                break

            # algorithm start
            if i == j:
                self._res_matrix[i][j] = 0
            else:
                self._res_matrix[i][j] = sys.maxsize
                for h in range(i, j):
                    self._res_matrix[i][j] = min(self._res_matrix[i][j],
                                                 self._res_matrix[i][h] + self._res_matrix[h + 1][j] + self._matrix_arr[i - 1] * self._matrix_arr[h] *
                                                 self._matrix_arr[j])
            # algorithm end

            i, j = i + 1, j + 1
            if j == len(self._matrix_arr):
                loop_count += 1
                i, j = 1, loop_count

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return self._res_matrix[1][len(self._matrix_arr) - 1]


def main():
    for inp in input_source:
        c = MCM(inp)
        print(c.res())


if __name__ == '__main__':
    main()
