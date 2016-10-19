""" Created by Jieyi on 8/18/16. """
from input_data.dynamic_programming.binomail_coefficient import input_source
from jieyi.algorithm.dynamic_programming import DP


class BC(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
    """

    def __init__(self, c1, c2):
        self._c1 = c1
        self._c2 = c2
        self._ans_matrix = [[0 for _ in range(c1 + 1)] for _ in range(c2 + 1)]

    def _backtracking(self):
        pass

    def _algorithm(self):
        for i in range(self._c2 + 1):
            for j in range(i, self._c1 + 1):
                self._ans_matrix[i][j] = 1 if i == j or i == 0 else self._ans_matrix[i - 1][j - 1] + self._ans_matrix[i][j - 1]

    def res(self):
        self._algorithm()
        print(self._ans_matrix[self._c2][self._c1])


def main():
    for c1, c2 in input_source:
        b = BC(c1, c2)
        b.res()


if __name__ == '__main__':
    main()
