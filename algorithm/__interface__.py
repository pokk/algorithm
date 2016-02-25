""" Created by wu.jieyi on 2016/02/24. """
from abc import ABCMeta
from functools import wraps
from time import time


def counting_time(fun):
    @wraps(fun)
    def wrap(*args, **kargs):
        t = time()
        res = fun(*args, **kargs)
        print(time() - t)
        return res

    return wrap


class Numeral(metaclass=ABCMeta):
    """
    For all of the numeral problem. We can get the result from each
    of the method.
    """

    def __init__(self):
        self._result_array = []
        self._array_size = len(self._result_array)
        pass

    def permutation(self, array):
        pass

    def combination(self, array):
        pass

    def _init_variable(self):
        del self._result_array
        self._result_array = []
        self._array_size = len(self._result_array)

    @staticmethod
    def _list_2_str(array):
        return array[:] if type(array) is str else ''.join(str(c) for c in array)


def main():
    print("hello world")


if __name__ == '__main__':
    main()
