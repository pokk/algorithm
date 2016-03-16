""" Created by wu.jieyi on 2016/02/24. """
from algorithm.__interface__ import Numeral


class Permutation(Numeral):
    def __init__(self):
        super().__init__()

    def permutation(self, array):
        self._init_variable()  # Always init the variables before process.
        arr = self._list_2_str(array)

        self.__recursive_permutation('', arr)
        # self.__non_recursive_permutation(arr)

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

    def __non_recursive_permutation(self, array):
        """
        Johnson–Trotter algorithm.
        1. Init two arrays from 0 to n-1 for calculate the direction and the position.
        2. Find the biggest movable number in the sequence.
           (Movable number: a number of direction is smaller than the number)
        3. Swap the biggest movable number and the number direction's number.
        4. Change all of the number's direction are smaller than the biggest movable number.

        :param array: Original array.
        """

        def max_movable():
            """
            Find the biggest movable number.

            :return: The biggest movable number.
            """

            max_movable_number = -1  # Default is minimum -1.
            for index in range(len(tmp_arr)):
                if index > 0 and tmp_dir[index] is -1:
                    if tmp_arr[index] > tmp_arr[index - 1]:
                        max_movable_number = max(max_movable_number, tmp_arr[index])
                elif index < len(tmp_arr) - 1 and tmp_dir[index] is 1:
                    if tmp_arr[index] > tmp_arr[index + 1]:
                        max_movable_number = max(max_movable_number, tmp_arr[index])

            return max_movable_number

        tmp_arr = [i for i in range(len(array))]  # Use virtual array instead of original array.
        tmp_dir = [-1 for _ in range(len(array))]  # All of the number of direction is -1(left).

        while 1:
            m = max_movable()
            self._result_array.append(''.join([array[int(i)] for i in tmp_arr]))
            if m is -1:
                break

            index_m = tmp_arr.index(m)
            # Swap the biggest number and the number direction's number.
            if tmp_dir[tmp_arr.index(m)] is -1:
                tmp_dir[index_m], tmp_dir[index_m - 1] = tmp_dir[index_m - 1], tmp_dir[index_m]
                tmp_arr[index_m], tmp_arr[index_m - 1] = tmp_arr[index_m - 1], tmp_arr[index_m]
            elif tmp_dir[tmp_arr.index(m)] is 1:
                tmp_dir[index_m], tmp_dir[index_m + 1] = tmp_dir[index_m + 1], tmp_dir[index_m]
                tmp_arr[index_m], tmp_arr[index_m + 1] = tmp_arr[index_m + 1], tmp_arr[index_m]

            # Reverse the direction.
            for number, direction in zip(tmp_arr, tmp_dir):
                if number > m:
                    direction *= -1


def main():
    a = 'ABCDEFG'

    per = Permutation()
    p = per.permutation(a)

    print(p)
    print(len(p))


if __name__ == '__main__':
    main()
