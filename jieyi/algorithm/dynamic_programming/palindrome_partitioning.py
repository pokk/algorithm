""" Created by Jieyi on 9/22/16. """
import sys

from input_data.dynamic_programming.palindrome_partitioning import input_source
from jieyi.algorithm.dynamic_programming import DP


class PP(DP):
    def __init__(self, palindrome):
        self._palindrome = palindrome
        self._res_matrix = [[0 for _ in range(len(self._palindrome))] for _ in range(len(self._palindrome))]

    def _preset(self):
        pass

    def _is_palindrome(self, string):
        for i in range(int(len(string) / 2)):
            if string[i] != string[-i - 1]:
                return False

        return True

    def _algorithm(self):
        i, j, loop_count = 0, 0, 0
        while True:
            if i == 0 and j == len(self._palindrome):
                break

            # algorithm start
            if i == j:
                self._res_matrix[i][j] = 0
            else:
                for h in range(i, j):
                    self._res_matrix[i][j] = sys.maxsize
                    self._res_matrix[i][j] = min(self._res_matrix[i][j],
                                                 1 + \
                                                 (0 if self._is_palindrome(self._palindrome[i:h + 1]) else self._res_matrix[i][h]) + \
                                                 (0 if self._is_palindrome(self._palindrome[h + 1:j + 1]) else self._res_matrix[h + 1][j]))
            # algorithm end

            i, j = i + 1, j + 1
            if j == len(self._palindrome):
                loop_count += 1
                i, j = 0, loop_count

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return self._res_matrix[0][len(self._palindrome) - 1]


def main():
    for inp in input_source:
        c = PP(inp)
        print(c.res())


if __name__ == '__main__':
    main()
