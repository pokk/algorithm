#!/usr/bin/env python3


def _lpm_recurrence(array, n, i, j):
    num = array[i][j] + 1
    if i + 1 < n:
        if array[i+1][j] == num:
            return _lpm_recurrence(array, n, i+1, j) + 1

    if j + 1 < n:
        if array[i][j+1] == num:
            return _lpm_recurrence(array, n, i, j+1) + 1

    if j > 0:
        if array[i][j-1] == num:
            return _lpm_recurrence(array, n, i, j-1) + 1

    if i > 0:
        if array[i-1][j] == num:
            return _lpm_recurrence(array, n, i-1, j) + 1

    return 1


def lpm_recurrence(array, n):
    best = 0

    for i in range(n):
        for j in range(n):
            result = _lpm_recurrence(array, n, i, j)
            if result > best:
                best = result

    return best


def _lpm_dp_table(array, table, n, i, j):
    num = array[i][j] + 1
    if i + 1 < n:
        if array[i+1][j] == num:
            if table[i+1][j]:
                table[i][j] = table[i+1][j] + 1
            else:
                table[i][j] = _lpm_dp_table(array, table, n, i+1, j) + 1
            return table[i][j]

    if j + 1 < n:
        if array[i][j+1] == num:
            if table[i][j+1]:
                table[i][j] = table[i][j+1] + 1
            else:
                table[i][j] = _lpm_dp_table(array, table, n, i, j+1) + 1
            return table[i][j]

    if j > 0:
        if array[i][j-1] == num:
            if table[i][j-1]:
                table[i][j] = table[i][j-1] + 1
            else:
                table[i][j] = _lpm_dp_table(array, table, n, i, j-1) + 1
            return table[i][j]

    if i > 0:
        if array[i-1][j] == num:
            if table[i-1][j]:
                table[i][j] = table[i-1][j] + 1
            else:
                table[i][j] = _lpm_dp_table(array, table, n, i-1, j) + 1
            return table[i][j]

    table[i][j] = 1

    return table[i][j]


def lpm_dp_table(array, n):
    dp_table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            _lpm_dp_table(array, dp_table, n, i, j)

    longest = 0

    for i in range(n):
        for j in range(n):
            longest = max(longest, dp_table[i][j])

    return longest


def qsort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0][0]
        return qsort([x for x in array[1:] if x[0] < pivot]) + \
               [pivot] + qsort([x for x in array[1:] if x[0] >= pivot])


def lpm_dp_table_by_sorting(array, n):
    sorting_table = []
    longest = 0

    for i in range(n):
        for j in range(n):
            sorting_table.append([array[i][j], (i, j)])

    qsort(sorting_table)

    dp_table = [[1 for _ in range(n)] for _ in range(n)]

    for _ in sorting_table:
        value, (i, j) = _[0], _[1]
        value -= 1
        if i + 1 < n:
            if array[i+1][j] == value:
                dp_table[i+1][j] = dp_table[i][j] + 1
                longest = max(longest, dp_table[i+1][j])
                continue

        if j + 1 < n:
            if array[i][j+1] == value:
                dp_table[i][j+1] = dp_table[i][j] + 1
                longest = max(longest, dp_table[i][j+1])
                continue

        if j > 0:
            if array[i][j-1] == value:
                dp_table[i][j-1] = dp_table[i][j] + 1
                longest = max(longest, dp_table[i][j-1])
                continue

        if i > 0:
            if array[i-1][j] == value:
                dp_table[i-1][j] = dp_table[i][j] + 1
                longest = max(longest, dp_table[i-1][j])
                continue
    return longest


def main():
    array = [[1, 2, 9],
             [5, 3, 8],
             [4, 6, 7]]

    print(lpm_dp_table_by_sorting(array, 3))

if __name__ == '__main__':
    main()
