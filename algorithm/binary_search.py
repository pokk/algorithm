""" Created by Jieyi on 2/14/16. """
from algorithm import arr


class BinarySearch:
    """
    Binary search. You could change the sorting method to other one.
    Just using find.
    """

    def __init__(self):
        pass

    @staticmethod
    def find(array_list, obj):
        b = BinarySearch()
        arr_temp = b.__sort(array_list[:])
        return b.__recursive_binary_search(arr_temp, obj)

    # Binary search for number.
    def __recursive_binary_search(self, array, obj):
        """
        1. Check the number of mid sequence.
        2. If the number of mid sequence is bigger than number what we wanna find,
           recursive searching in the right sequence. Otherwise, recursive searching
           the left sequence.
        3. Got a number we found, or none.
        """

        if len(array) is 0:
            return None

        mid_index = int(len(array) / 2)

        if obj > array[mid_index]:
            return self.__recursive_binary_search(array[mid_index + 1:], obj)
        elif obj < array[mid_index]:
            return self.__recursive_binary_search(array[:mid_index], obj)
        elif obj == array[mid_index]:
            return array[mid_index]

    # Default sort method. (Bubble sort)
    # You can change to other sorting methods.
    def __sort(self, array, sort_method=None):
        if sort_method is None:
            self.bubble_sort(array)
        else:
            sort_method(array)

        return array

    # Bubble sort. The easiest sorting method.
    @staticmethod
    def bubble_sort(array):
        """ Algorithm
        1. Compare two numbers, put the bigger one to right side.
        2. Sequence doing step 1. Finally, you can put the biggest one to the rightest side.
        3. Continue step 1, 2 until to the end.
        4. Got an order sequence.

        :param array: A number sequence without sorting.
        """
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


def main():
    print(BinarySearch.find(arr, 56))


if __name__ == '__main__':
    main()
