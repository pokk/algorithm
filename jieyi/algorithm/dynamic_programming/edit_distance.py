""" Created by wujieyi on 06/16/2016. """
from input_data.dynamic_programming.edit_distance import input_source
from jieyi.algorithm.dynamic_programming import DP
from jieyi.algorithm.dynamic_programming.suffix_matrix import SuffixMatrix


class ED(DP):
    """
    Dynamic Programming
    The problem's description is as below.
    http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
    """

    def __init__(self, str1=None, str2=None):
        self._suffix_matrix = SuffixMatrix(str1, str2)
        self._matrix = self._suffix_matrix.suffix_matrix
        self._str1 = str1
        self._str2 = str2

    def _init_matrix(self):
        """
        Initialize the suffix matrix.
        """

        for i in range(len(self._str1) + 1):
            self._matrix[0][i]['len'] = i
        for j in range(len(self._str2) + 1):
            self._matrix[j][0]['len'] = j

    def _algorithm(self):
        """
        Edit Distance algorithm.
        """

        for i, s in enumerate(self._str2):
            for j, t in enumerate(self._str1):
                if s == t:
                    self._matrix[i + 1][j + 1]['len'] = self._matrix[i][j].get('len')
                    self._matrix[i + 1][j + 1]['direct'] = 'ul'
                else:
                    self._matrix[i + 1][j + 1]['len'] = \
                        min(self._matrix[i + 1][j].get('len'), self._matrix[i][j + 1].get('len'),
                            self._matrix[i][j].get('len')) + 1

    def _backtracking(self):
        pass

    def res(self):
        self._init_matrix()
        self._algorithm()

        return self._matrix[len(self._str2)][len(self._str1)].get('len')

    def show_matrix(self):
        self._suffix_matrix.show_suffix()


def main():
    for ed in input_source:
        res = ED(ed[0], ed[1])
        print(res.res())


if __name__ == '__main__':
    main()
