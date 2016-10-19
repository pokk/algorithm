""" Created by Jieyi on 9/22/16. """
import sys

from input_data.dynamic_programming.minimum_insertions_palindrome import input_source
from jieyi.algorithm.dynamic_programming import DP


class MIP(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/
    """

    def __init__(self, string):
        self._half_palindrome = string
        self._res_matrix = [[0 for _ in range(len(self._half_palindrome))] for _ in range(len(self._half_palindrome))]

    def _preset(self):
        # We need to cut origin palindrome from half palindrome.
        tmp_palindrome = self._half_palindrome
        for i in range(int(len(self._half_palindrome) / 2)):
            if self._half_palindrome[i] == self._half_palindrome[-i - 1]:
                tmp_palindrome = tmp_palindrome[1: len(tmp_palindrome) - 1]
            else:
                break
        self._half_palindrome = tmp_palindrome

    def _is_palindrome(self, string):
        for i in range(int(len(string) / 2)):
            if string[i] != string[-i - 1]:
                return False

        return True

    def _algorithm(self):
        # This algorithm is totally same as palindrome partitioning, but the meaning is difference.
        i, j, loop_count = 0, 0, 0
        while True:
            if i == 0 and j == len(self._half_palindrome):
                break

            # algorithm start
            if i == j:
                self._res_matrix[i][j] = 0
            else:
                for h in range(i, j):
                    self._res_matrix[i][j] = sys.maxsize
                    self._res_matrix[i][j] = min(self._res_matrix[i][j],
                                                 1 + \
                                                 (0 if self._is_palindrome(self._half_palindrome[i:h + 1]) else self._res_matrix[i][h]) + \
                                                 (0 if self._is_palindrome(self._half_palindrome[h + 1:j + 1]) else self._res_matrix[h + 1][j]))
            # algorithm end

            i, j = i + 1, j + 1
            if j == len(self._half_palindrome):
                loop_count += 1
                i, j = 0, loop_count

    def _backtracking(self):
        pass

    def res(self):
        self._preset()
        self._algorithm()

        return self._res_matrix[0][len(self._half_palindrome) - 1]


def main():
    for inp in input_source:
        c = MIP(inp)
        print(c.res())


if __name__ == '__main__':
    main()
