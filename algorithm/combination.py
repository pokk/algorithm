""" Created by wu.jieyi on 2016/02/24. """
from algorithm.__interface__ import Numeral


class Combination(Numeral):
    def __init__(self):
        super().__init__()

    def combination(self, array):
        self._init_variable()
        arr = self._list_2_str(array)

        # self.__recursive_combination_order_pick('', arr)
        # self.__recursive_combination_choose('', arr)
        self.__nonrecursive_combination(arr)

        return self._result_array

    def __recursive_combination_order_pick(self, res, array, index=0):
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
            self.__recursive_combination_order_pick(res + array[i], array, i + 1)

    def __recursive_combination_choose(self, res, array, index=0):
        """
        Each of round we decide we will pick this index of character or not.
        For example as below:
                        ooo
                       'ABC'
                  oo  /
                 'ABC'
            o   /     \ oox
           'ABC'       'ABC'
          /     \ ox
        ''       'ABC'
          \ x
           'ABC'

        :param res: One of the combination of the result.
        :param array: Original array.
        :param index: Original array's index.
        """

        if index is len(array):
            self._result_array.append(res)
        else:
            self.__recursive_combination_choose(res + array[index], array, index + 1)
            self.__recursive_combination_choose(res, array, index + 1)

    def __nonrecursive_combination(self, array):
        # There is an empty set in the combination.
        self._result_array.append('')

        for buff in range(len(array) + 1):
            for i in range(len(array) - buff):
                times = range(1) if buff is 0 else range(i + buff, len(array))
                for j in times:
                    print(array[i:i + buff + 1] if j is 0 else array[i:i + buff] + array[j])
                    self._result_array.append(array[i:i + buff + 1] if j is 0 else array[i:i + buff] + array[j])


def main():
    c = Combination()
    a = c.combination('ABCD')

    print(a)
    print(len(a))


if __name__ == '__main__':
    main()
