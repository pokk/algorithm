""" Created by Jieyi on 2/11/16. """
import random


class Stack:
    def __init__(self):
        self.__stack = []

    def pop(self):
        if self.is_empty():
            return None

        obj = self.__stack[len(self.__stack) - 1]
        self.__stack = self.__stack[:len(self.__stack) - 1]
        return obj

    def push(self, obj):
        self.__stack.append(obj)

    def is_empty(self):
        if len(self.__stack) is 0:
            return True
        return False

    def show(self):
        print(self.__stack)


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
