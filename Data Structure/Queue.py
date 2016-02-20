""" Created by Jieyi on 2/11/16. """
import random


class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, obj):
        self.__queue.append(obj)

    def dequeue(self):
        if self.is_empty():
            return None

        tmp = self.__queue[0]
        self.__queue = self.__queue[1:]
        return tmp

    def is_empty(self):
        return True if len(self.__queue) is 0 else False

    def show(self):
        print(self.__queue)


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
