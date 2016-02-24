""" Created by wu.jieyi on 2016/02/24. """
from abc import ABCMeta


class Numeral(metaclass=ABCMeta):
    """
    For all of the numeral problem. We can get the 
    """

    def __init__(self):
        self._result_array = []
        self._array_size = len(self._result_array)
        pass

    def permutation(self, array):
        pass

    def combination(self, array):
        pass


def main():
    print("hello world")


if __name__ == '__main__':
    main()
