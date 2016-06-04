""" Created by Jieyi on 6/4/16. """
from copy import deepcopy


class LCS:
    def __init__(self, str1=None, str2=None):
        self._str1 = str1
        self._str2 = str2
        self._lcs = []
        self._suffix_array = []

    def _init_suffix(self):
        tmp = []
        value = {'direct': 'x', 'len': 0}
        for _ in self._str2:
            tmp.clear()
            tmp.append(deepcopy(value))  # pre-advanced.
            for _ in self._str1:
                tmp.append(deepcopy(value))
            self._suffix_array.append(deepcopy(tmp))
        self._suffix_array.append(deepcopy(tmp))  # pre-advanced.

    def _make_suffix_array(self, str1, str2):
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
        problem:
        1. switch case return by dict.
        2. array size.
        """

        def inner_backtracking(i, j):
            print(i, j)
            # if self._suffix_array[i][j]['direct'] == 'x':
            #     return
            if self._suffix_array[i][j]['direct'] == 'ul':
                print(i, j)
                inner_backtracking(i - 1, j - 1)
            elif self._suffix_array[i][j]['direct'] == 'u':
                inner_backtracking(i - 1, j)
            elif self._suffix_array[i][j]['direct'] == 'l':
                inner_backtracking(i, j - 1)

        inner_backtracking(len(self._str1), len(self._str2))
        print()

    def res(self):
        self._init_suffix()
        self._make_suffix_array(self._str1, self._str2)
        self._backtracking()

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
                print(t, sep='', end=' ')
            print()


def main():
    str1 = "fdaifadshi"
    str2 = "fdaa"
    lcs = LCS(str1, str2)
    lcs.res()

    # lcs.show_suffix()


if __name__ == '__main__':
    main()
