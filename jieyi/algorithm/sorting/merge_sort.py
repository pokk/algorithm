""" Created by Jieyi on 2/14/16. """
from algorithm import arr


class MergeSort:
    """
    Merge sort.
    """

    def __init__(self):
        pass

    @staticmethod
    def sort(arr_list):
        ms = MergeSort()
        return ms.__merge_sort(arr_list[:])

    # Merge sort, always divide two balance sequences.
    def __merge_sort(self, arr_list):
        """ Algorithm
        1. Divide two balance sequences.
        2. Recursive merge sort in left sequence.
        3. Recursive merge sort in right sequence.
        4. Merge the left and right sequence.
        5. Got an order sequence.
        """

        if len(arr_list) > 1:
            mid_index = int(len(arr_list) / 2)

            left = self.__merge_sort(arr_list[:mid_index])
            right = self.__merge_sort(arr_list[mid_index:])
            return self.__merge(left, right)
        return arr_list

    # Core code of merge sort.
    def __merge(self, left, right):
        """ Algorithm
        1. 'left' is a main sequence.
        2. 'right' is a sub sequence.
        3. Check if 'right' number is smaller than 'left' number or not.
           If 'Yes', the number insert to current index of 'left'. Otherwise, go next of 'left'.
        4. If 'left' is finished visiting, we add all of the 'right' to the end of 'left'.
        """

        if len(left) is 0:
            return right
        elif len(right) is 0:
            return left

        main_index = 0
        for sub_arr_num in right:
            for main_index in range(main_index, len(left)):
                if sub_arr_num <= left[main_index]:
                    left.insert(main_index, sub_arr_num)
                    break
                main_index += 1

            if main_index is len(left):
                left.append(sub_arr_num)

        return left


def main():
    arr_list = MergeSort.sort(arr)
    print(arr_list)


if __name__ == '__main__':
    main()
