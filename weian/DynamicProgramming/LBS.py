#!/usr/bin/env python3


def LIS(array):
    length = len(array)
    result = []
    for _ in range(length):
        result.append(1)

    for i in range(length):
        for j in range(i+1, length):
            if array[i] < array[j]:
                result[j] = max(result[j], result[i]+1)

    lis = -1
    for _ in result:
        lis = max(lis, _)

    return lis, result


# longest bitonic subsequence
def LBS(array):
    # LIS
    lis_num, lis_array = LIS(array)

    # LDS
    lds_num, lds_array = LIS(array[::-1])
    lds_array = lds_array[::-1]

    result = []
    for _ in range(len(array)):
        print(str(lis_array[_]) + " " + str(lds_array[_]))
        result.append(lis_array[_] + lds_array[_] - 1)

    lbs = -1
    for _ in result:
        lbs = max(lbs, _)

    return lbs


def main():
    a = [3, 4, -1, 0, 6, 2, 3]
    print(LBS(a))

if __name__ == "__main__":
    main()
