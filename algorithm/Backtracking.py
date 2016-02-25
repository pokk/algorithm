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


def recursive_eight_queen(square, index_x=0, index_y=0, queens=0):
    if index_x is 0 and index_y is len(square):
        for q in square:
            print(q)
        print()
        return

    square[index_x][index_y] = 1
    recursive_eight_queen(square, (index_x + 1) % len(square), index_y + 1 if int((index_x + 1) / len(square)) is 1 else index_y, queens + 1)
    square[index_x][index_y] = 0
    recursive_eight_queen(square, (index_x + 1) % len(square), index_y + 1 if int((index_x + 1) / len(square)) is 1 else index_y, queens)


def main():
    # recursive_permutation([], 3)
    recursive_eight_queen([[0, 0], [0, 0]])


if __name__ == '__main__':
    main()
