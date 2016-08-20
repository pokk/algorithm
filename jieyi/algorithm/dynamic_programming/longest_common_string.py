""" Created by Jieyi on 6/4/16. """

from input_data.dynamic_programming.longest_common_string import input_source
from jieyi.algorithm.dynamic_programming import DP
from jieyi.algorithm.dynamic_programming.suffix_matrix import SuffixMatrix


class LCS(DP):
    """
    Counting and calculate the longest common string algorithm.
    """

    def __init__(self, str1=None, str2=None):
        self._suffix_matrix = SuffixMatrix(str1, str2)
        self._matrix = self._suffix_matrix.suffix_matrix
        self._str1 = str1
        self._str2 = str2
        self._lcs = []

    def _algorithm(self):
        """
        LCS algorithm.
        """

        for i, s in enumerate(self._str2):
            for j, t in enumerate(self._str1):
                if t == s:
                    self._matrix[i + 1][j + 1]['len'] = self._matrix[i][j].get('len') + 1
                    self._matrix[i + 1][j + 1]['direct'] = 'ul'
                else:
                    self._matrix[i + 1][j + 1]['len'] = \
                        max(self._matrix[i + 1][j].get('len'), self._matrix[i][j + 1].get('len'))
                    self._matrix[i + 1][j + 1]['direct'] = \
                        'l' if self._matrix[i + 1][j].get('len') >= self._matrix[i][j + 1].get('len') else 'u'

    def _backtracking(self):
        """
        using backtracking to find the lcs.
        """

        def inner_backtracking(i, j):
            {
                'ul': lambda: (inner_backtracking(i - 1, j - 1),
                               self._lcs.append(self._str1[j - 1])),
                'u': lambda: inner_backtracking(i - 1, j),
                'l': lambda: inner_backtracking(i, j - 1)
            }.get(self._matrix[i][j]['direct'], lambda: None)()

        inner_backtracking(len(self._str2), len(self._str1))

    def res(self):
        """
        running the lcs algorithm and backtracking for getting the result.

        :return: (lcs length, lcs string)
        """

        self._algorithm()
        self._backtracking()
        return self._matrix[len(self._str2)][len(self._str1)].get('len'), ''.join(self._lcs)

    def show_matrix(self):
        self._suffix_matrix.show_suffix()


def main():
    for lcs in input_source:
        l = LCS(lcs[0], lcs[1])
        print(l.res())


if __name__ == '__main__':
    main()
