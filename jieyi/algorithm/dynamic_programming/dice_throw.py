""" Created by Jieyi on 9/22/16. """
from input_data.dynamic_programming.dice_throw import input_source
from jieyi.algorithm.dynamic_programming import DP


class DT(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dice-throw-problem/
    """

    def __init__(self, inp):
        self._faces = inp[0]
        self._dices = inp[1]
        self._sum = inp[2]
        self._res_matrix = [[0 for _ in range(self._sum + 1)] for _ in range(self._dices + 1)]

    def _preset(self):
        for i in range(1, self._faces + 1):
            if i > self._sum:
                break
            self._res_matrix[1][i] = 1

    def _algorithm(self):
        for i in range(1, self._dices + 1):
            for j in range(1, self._sum + 1):
                for s in range(1, self._faces + 1):
                    if s >= self._sum:
                        continue
                    if j >= s:
                        self._res_matrix[i][j] += self._res_matrix[i - 1][j - s]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return self._res_matrix[len(self._res_matrix) - 1][len(self._res_matrix[0]) - 1]


def main():
    for inp in input_source:
        c = DT(inp)
        print(c.res())


if __name__ == '__main__':
    main()
