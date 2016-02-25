""" Created by wu.jieyi on 2016/02/24. """
from algorithm.__interface__ import Numeral


class Permutation(Numeral):
    def __init__(self):
        super().__init__()

    def permutation(self, array):
        self._init_variable()  # Always init the variables before process.
        arr = self._list_2_str(array)

        self.__recursive_permutation('', arr)

        return self._result_array

    def __recursive_permutation(self, res, array):
        """
        Pick up the character sequentially and do the recursive.
        For example as below:
                    'A', 'BC'   'BA', 'C' - 'BAC', ''
                  /           /
        '', 'ABC' - 'B', 'AC'
                  \           \
                    'C', 'AB'   'BC', 'A' - 'BCA', ''

        :param res: One of the result of permutation.
        :param array: Original array.
        """
        if not array:
            self._array_size += 1
            self._result_array.append(res)
        else:
            for i in range(len(array)):
                self.__recursive_permutation(res + array[i], array[:i] + array[i + 1:])


def main():
    a = 'ABCD'

    per = Permutation()
    p = per.permutation(a)

    print(p)
    print(len(p))


if __name__ == '__main__':
    main()
