""" Created by wu.jieyi on 2016/02/24. """
from __interface__ import Numeral


class Combination(Numeral):
    def __init__(self):
        super().__init__()

    def combination(self, array):
        self._init_variable()
        arr = self._list_2_str(array)

        self.__recursive_combination('', arr)

        return self._result_array

    def __recursive_combination(self, res, array, index=0):
        """
        We continue the index from previous round and pick up this index of
        character to add into the result. We can get combination from each
        of node.
        For example as below:
                         (2) 'AB' -(3) 'ABC'
                        /
                (1) 'A' -(3) 'AC'
               /
        (0) '' -(2) 'B' -(3) 'BC'
               \
                (3) 'C'

        :param res: One of the combination of the result.
        :param array: Original array.
        :param index: Each of recursive step of index.
        """
        self._result_array.append(res)
        for i in range(index, len(array)):
            self.__recursive_combination(res + array[i], array, i + 1)


def main():
    c = Combination()
    a = c.combination('ABC')

    print(a)
    print(len(a))


if __name__ == '__main__':
    main()
