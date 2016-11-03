""" Created by Jieyi on 11/2/16. """
from input_data.dynamic_programming.maximum_size_square_submatrix import input_source
from jieyi.algorithm.dynamic_programming import DP


class MSSS(DP):
    """
    Maximum size square sub-matrix with all 1s.
    The problem's url is as below.
    http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
    """

    def __init__(self, map):
        self._map = map
        self._max_square = 0

    def _preset(self):
        self._matrix = [[0 for _ in range(len(self._map[0]) + 1)]]
        for row in self._map:
            self._matrix.append([0] + row)

        self._ans_matrix = [[0 for _ in range(len(self._matrix[_]))] for _ in range(len(self._matrix))]

    def _algorithm(self):
        for i in range(1, len(self._matrix)):
            for j in range(1, len(self._matrix[i])):
                if 1 == self._matrix[i][j]:
                    self._ans_matrix[i][j] = min(self._ans_matrix[i - 1][j - 1], self._ans_matrix[i][j - 1], self._ans_matrix[i - 1][j]) + 1
                    self._max_square = max(self._max_square, self._ans_matrix[i][j])

        return self._max_square

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = MSSS(inp)
        print(c.res())


if __name__ == '__main__':
    main()
