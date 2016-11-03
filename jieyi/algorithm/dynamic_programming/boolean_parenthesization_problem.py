""" Created by Jieyi on 11/2/16. """
import operator

from input_data.dynamic_programming.boolean_parenthesization_problem import input_source
from jieyi.algorithm.dynamic_programming import DP


class BPP(DP):
    """
    Boolean Parenthesization Problem.
    The problem's url is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/
    """

    def __init__(self, source):
        self._symbols = source[0]
        self._operators = source[1]
        self._true_matrix = [[0 for _ in range(len(self._symbols))] for _ in range(len(self._symbols))]
        self._false_matrix = [[0 for _ in range(len(self._symbols))] for _ in range(len(self._symbols))]

    def _preset(self):
        pass

    def _algorithm(self):
        def and_operator():
            return self._true_matrix[i][h] * self._true_matrix[h + 1][j], \
                   (self._true_matrix[i][h] + self._false_matrix[i][h]) * (self._true_matrix[h + 1][j] + self._false_matrix[h + 1][j]) - \
                   self._true_matrix[i][h] * self._true_matrix[h + 1][j]

        def or_operator():
            return (self._true_matrix[i][h] + self._false_matrix[i][h]) * (self._true_matrix[h + 1][j] + self._false_matrix[h + 1][j]) - \
                   self._false_matrix[i][h] * self._false_matrix[h + 1][j], \
                   self._false_matrix[i][h] * self._false_matrix[h + 1][j]

        def xor_operator():
            return self._true_matrix[i][h] * self._false_matrix[h + 1][j] + self._false_matrix[i][h] * self._true_matrix[h + 1][j], \
                   self._true_matrix[i][h] * self._true_matrix[h + 1][j] + self._false_matrix[i][h] * self._false_matrix[h + 1][j]

        i, j, loop_count = 0, 0, 0
        while True:
            if i == 0 and j == len(self._true_matrix):
                break

            # algorithm start
            if i == j:
                self._true_matrix[i][j] = 1 if self._symbols[i] else 0
                self._false_matrix[i][j] = 1 if not self._symbols[i] else 0
            else:
                true_count = 0
                false_count = 0
                for h in range(i, j):
                    true_count, false_count = list(map(operator.add, (true_count, false_count), {
                        '|': or_operator,
                        '&': and_operator,
                        '^': xor_operator,
                    }.get(self._operators[h])()))
                self._true_matrix[i][j] = true_count
                self._false_matrix[i][j] = false_count
            # algorithm end

            i, j = i + 1, j + 1
            if j == len(self._true_matrix):
                loop_count += 1
                i, j = 0, loop_count

        return self._true_matrix[0][-1]

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        return self._algorithm()


def main():
    for inp in input_source:
        c = BPP(inp)
        print(c.res())


if __name__ == '__main__':
    main()
