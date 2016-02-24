""" Created by Jieyi on 2/11/16. """
import random


class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, obj):
        self.__list.append(obj)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__list.pop(0)

    def is_empty(self):
        return not self.__list

    def show(self):
        print(self.__list)


def main():
    q = Queue()

    for i in range(8):
        q.enqueue(random.randint(0, 30))
    q.show()

    for i in range(3):
        print(q.dequeue())
    q.show()


if __name__ == '__main__':
    main()
