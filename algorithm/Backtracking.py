""" Created by wu.jieyi on 2016/02/23. """


def recursive_permutation_limit(res, depth, level=0):
    """
    [0, 0, 0] ~ [3, 3, 3]
    Show all of the permutation result.

    :param res: result of permutation.
    :param depth: how many bits of permutation.
    :param level: recursive level.
    """
    if level >= depth:
        print(res)
    else:
        for i in range(1, 3 + 1):
            recursive_permutation_limit(res + [i], depth, level + 1)


count = 0
size = 4
col, row = [False] * size, [False] * size
left_diagonal, right_diagonal = [False] * size * 2, [False] * size * 2


def recursive_eight_queen(square, index_x=0, index_y=0, queens=0):
    """
    1. Consider the case, put or not put in each of the checkerboard.
    2. If put, we make a mark in this row, col, left diagonal, and right diagonal.
    3. Recursive this case until finishing all of the checkerboard.
    """

    global count, col, row, left_diagonal, right_diagonal

    # The end of chess.
    if index_y is len(square):
        # Satisfy queen's numbers.
        if queens is len(square):
            for q in range(len(square)):
                print(square[q])
            print()
        return

    # Counting the left diagonal's or the right diagonal's position.
    l_d, r_d = (index_x + index_y) % (len(square) * 2 - 1), (index_x - index_y + len(square) * 2) % (len(square) * 2 - 1)

    # Pruning the unnecessary steps.
    if not col[index_y] and not row[index_x] and not left_diagonal[l_d] and not right_diagonal[r_d]:
        # Make a mark which a queen is occupied.
        col[index_y] = row[index_x] = left_diagonal[l_d] = right_diagonal[r_d] = True

        square[index_y][index_x] = 1
        recursive_eight_queen(square, (index_x + 1) % len(square), index_y + 1 if int((index_x + 1) / len(square)) is 1 else index_y, queens + 1)

        # Delete a mark.
        col[index_y] = row[index_x] = left_diagonal[l_d] = right_diagonal[r_d] = False

    square[index_y][index_x] = 0
    recursive_eight_queen(square, (index_x + 1) % len(square), index_y + 1 if int((index_x + 1) / len(square)) is 1 else index_y, queens)


def main():
    arr = [[0 for _ in range(size)] for _ in range(size)]
    recursive_eight_queen(arr)


if __name__ == '__main__':
    main()
