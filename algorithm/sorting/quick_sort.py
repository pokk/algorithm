""" Created by Jieyi on 2/14/16. """
from algorithm import arr


class QuickSort:
    """
    Quick Sort.
    """

    def __init__(self):
        pass

    @staticmethod
    def sort(arr_list):
        qs_arr = arr_list[:]
        qs = QuickSort()
        # qs.__quick_sort(qs_arr, 0, len(qs_arr) - 1)
        qs_arr = qs.__q_sort(qs_arr)

        return qs_arr

    # Normal quick sort algorithm.
    def __quick_sort(self, arr_list, l_index, r_index):
        """ Algorithm
        1. Choose a pivot for dividing two sequence.
        2. Search a number is smaller than pivot from the leftest to right.
        3. Search a number is larger than pivot from the rightest to left.
        4. Swap the two number. Continue step 2 and step 3 until cross.
        5. Let the pivot divide two sequence, all of the number in left side are smaller than pivot,
           in the other hand, do the same thing.
        6. Left side sequence does quick sort by recursive. Right side also do.
        5. Got an order sequence.
        """

        if l_index >= r_index:
            return

        split_num = arr_list[int((l_index + r_index) / 2)]
        l = l_index
        r = r_index

        while True:
            while l <= r_index:
                if arr_list[l] > split_num:
                    break
                l += 1

            while r > l_index:
                if split_num > arr_list[r]:
                    break
                r -= 1

            if l > r:
                break

            arr_list[l], arr_list[r] = arr_list[r], arr_list[l]

        arr_list[l_index], arr_list[r] = arr_list[r], arr_list[l_index]

        self.__quick_sort(arr_list, l_index, r - 1)
        self.__quick_sort(arr_list, l, r_index)

    # Using quick sort concept.
    def __q_sort(self, arr_list):
        """ Algorithm
        1. All of number is smaller than pivot put to left side.
        2. All of number is larger than pivot put to right side.
        3. Left sequence does the quick sort by recursive, Right sequence does the quick sort by recursive.
        4. Got an order sequence.
        """

        if len(arr_list) <= 1:
            return arr_list
        else:
            split_num = arr_list[0]
            return self.__q_sort([l for l in arr_list[1:] if l < split_num]) + [split_num] + self.__q_sort(
                [r for r in arr_list[1:] if r >= split_num])


def main():
    q_arr = QuickSort.sort(arr)
    print(q_arr)


if __name__ == '__main__':
    main()
