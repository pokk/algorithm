"""
http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
2016/7/5
author: weian
"""
#!/usr/bin/env python3

from copy import copy
from input_data.dynamic_programming.subset_sum_problem import q2


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])


def Subset_Sum_Problem(array, q):
    array = qsort(array)
    print(array)
    result_set = []
    maybe_set = []

    s = sum(array)
    if s < q:
        return False, None
    elif s == q:
        return True, array

    for i in range(len(array)):
        need = q
        for _ in range(i, len(array)):
            if need - array[_] > 0:
                maybe_set.append(array[_])
                need -= array[_]
            elif need - array[_] == 0:
                maybe_set.append(array[_])
                need = 0
                break

        if need > 0:
            del maybe_set[:]

        if len(maybe_set) > 0:
            result_set.append(copy(maybe_set))
            del maybe_set[:]

    if len(result_set) > 0:
        return True, result_set
    else:
        return False, None


def main():
    print(Subset_Sum_Problem(q2[0], q2[1]))

if __name__ == '__main__':
    main()
