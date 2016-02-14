""" Created by Jieyi on 2/11/16. """
import random


class Queue:
    def __init__(self):
        self.__queue = []
        pass

    def enqueue(self, obj):
        self.__queue.append(obj)

    def dequeue(self):
        tmp = self.__queue[0]
        self.__queue = self.__queue[1:]
        return tmp

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
