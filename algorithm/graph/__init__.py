""" Created by wu.jieyi on 2016/03/23. """
import sys

arr_map = [[0, 4, 2, sys.maxsize, sys.maxsize, sys.maxsize],
           [1, 0, sys.maxsize, 2, sys.maxsize, sys.maxsize],
           [sys.maxsize, 3, 0, sys.maxsize, 5, sys.maxsize],
           [sys.maxsize, sys.maxsize, 4, 0, sys.maxsize, 2],
           [sys.maxsize, sys.maxsize, sys.maxsize, 1, 0, sys.maxsize],
           [sys.maxsize, 4, 5, sys.maxsize, 3, 0]]


def main():
    for i in range(len(arr_map)):
        for j in range(len(arr_map[i])):
            print(arr_map[i][j] if arr_map[i][j] is not sys.maxsize else '∞', end=' ')
        print()


if __name__ == '__main__':
    main()
