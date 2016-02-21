""" Created by Jieyi on 2/11/16. """
import random


class Stack:
    def __init__(self):
        self.__list = []

    def pop(self):
        if self.is_empty():
            return None

        obj = self.__list[len(self.__list) - 1]
        self.__list = self.__list[:len(self.__list) - 1]
        return obj

    def push(self, obj):
        self.__list.append(obj)

    def is_empty(self):
        return len(self.__list) is 0

    def show(self):
        print(self.__list)


def main():
    q = Stack()

    for i in range(8):
        q.push(random.randint(0, 30))
    q.show()

    for i in range(3):
        print(q.pop())
    q.show()


if __name__ == '__main__':
    main()
