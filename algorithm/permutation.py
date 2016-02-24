""" Created by wu.jieyi on 2016/02/24. """
from algorithm.__interface__ import Numeral


class Permutation(Numeral):
    def __init__(self):
        super().__init__()

    def permutation(self, array):
        arr = array[:] if type(array) is str else ''.join(str(c) for c in array)
        self.__init_var()
        self.__recursive_permutation('', arr)

        return self._result_array

    def __recursive_permutation(self, res, array):
        if not array:
            self._array_size += 1
            self._result_array.append(res)
        else:
            for i in range(len(array)):
                self.__recursive_permutation(res + array[i], array[:i] + array[i + 1:])

    def __init_var(self):
        del self._result_array
        self._result_array = []
        self._array_size = len(self._result_array)

    @property
    def get_array_size(self):
        return self._array_size


def main():
    a = 'ABC'

    per = Permutation()
    p = per.permutation(a)
    s = per.get_array_size
    print(p, s)


if __name__ == '__main__':
    main()
