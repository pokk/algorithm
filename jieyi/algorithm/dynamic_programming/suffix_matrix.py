""" Created by wujieyi on 06/16/2016. """
from copy import deepcopy


class SuffixMatrix:
    def __init__(self, str1=None, str2=None):
        self._str1 = str1
        self._str2 = str2
        self._suffix_matrix = []

        self._init_suffix()

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
            self._suffix_matrix.append(deepcopy(tmp))
        self._suffix_matrix.append(deepcopy(tmp))  # pre-advanced.

        return self._suffix_matrix

    def show_suffix(self):
        """
        Show the suffix matrix.
        """

        # adjust the view in the console.
        print("", end='    ')
        for s in self._str1:
            print(s, end=' ')
        print()

        for i, s in enumerate(self._suffix_matrix):
            # adjust the view in the console.
            if 0 < i <= len(self._str2):
                print(self._str2[i - 1], end=' ')
            else:
                print('', end='  ')

            for t in s:
                print(t.get('len'), sep='', end=' ')
            print()

    @property
    def suffix_matrix(self):
        return self._suffix_matrix


def main():
    print("Hello Python")


if __name__ == '__main__':
    main()
