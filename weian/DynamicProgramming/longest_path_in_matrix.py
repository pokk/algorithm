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


def main():
    array = [[1, 2, 9],
             [5, 3, 8],
             [4, 6, 7]]

    print(lpm_dp_table(array, 3))

if __name__ == '__main__':
    main()
