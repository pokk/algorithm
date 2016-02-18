""" Created by Jieyi on 2/14/16. """

arr = [3, 7, 2, 6, 1, 4, 532, 54, 41, 43]


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
        arr = b.__sort(array_list[:])
        return b.__recursive_binary_search(arr, obj)

    def __recursive_binary_search(self, array, obj):
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
    def __sort(self, array, sort_method=None):
        if sort_method is None:
            self.__bubble_sort(array)
        else:
            sort_method(array)

        return array

    def __bubble_sort(self, array):
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


def main():
    print(BinarySearch.find(arr, 56))


if __name__ == '__main__':
    main()
