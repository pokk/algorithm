""" Created by Jieyi on 6/4/16. """
from copy import deepcopy

from input_data.dynamic_programming.longest_common_string import lcs_str1, lcs_str2


class LCS:
    """
    Counting and calculate the longest common string algorithm.
    """

    def __init__(self, str1=None, str2=None):
        self._str1 = str1
        self._str2 = str2
        self._lcs = []
        self._suffix_array = []

    def _init_suffix(self):
        """
        initialize the suffix array.
        """

        tmp = []
        value = {'direct': 'x', 'len': 0}

        for _ in self._str2:  # for out-side.
            tmp.clear()
            tmp.append(deepcopy(value))  # pre-advanced.
            for _ in self._str1:  # for in-side.
                tmp.append(deepcopy(value))
            self._suffix_array.append(deepcopy(tmp))
        self._suffix_array.append(deepcopy(tmp))  # pre-advanced.

    def _make_suffix_array(self, str1, str2):
        """
        LCS algorithm.

        :param str1: comparing string.
        :param str2: comparing string.
        """

        for i, s in enumerate(str2):
            for j, t in enumerate(str1):
                if t == s:
                    self._suffix_array[i + 1][j + 1]['len'] = self._suffix_array[i][j].get('len') + 1
                    self._suffix_array[i + 1][j + 1]['direct'] = 'ul'
                else:
                    self._suffix_array[i + 1][j + 1]['len'] = \
                        max(self._suffix_array[i + 1][j].get('len'), self._suffix_array[i][j + 1].get('len'))
                    self._suffix_array[i + 1][j + 1]['direct'] = \
                        'l' if self._suffix_array[i + 1][j].get('len') >= self._suffix_array[i][j + 1].get('len') else 'u'

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
            }.get(self._suffix_array[i][j]['direct'], lambda: None)()

        inner_backtracking(len(self._str2), len(self._str1))

    def res(self):
        """
        running the lcs algorithm and backtracking for getting the result.

        :return: (lcs length, lcs string)
        """
        self._init_suffix()
        self._make_suffix_array(self._str1, self._str2)
        self._backtracking()
        return self._suffix_array[len(self._str2)][len(self._str1)].get('len'), ''.join(self._lcs)

    def show_suffix(self):
        # adjust the view in the console.
        print("", end='    ')
        for s in self._str1:
            print(s, end=' ')
        print()

        for i, s in enumerate(self._suffix_array):
            # adjust the view in the console.
            if 0 < i <= len(self._str2):
                print(self._str2[i - 1], end=' ')
            else:
                print('', end='  ')

            for t in s:
                print(t.get('len'), sep='', end=' ')
            print()


def main():
    lcs = LCS(lcs_str1, lcs_str2)
    print(lcs.res())


if __name__ == '__main__':
    main()
