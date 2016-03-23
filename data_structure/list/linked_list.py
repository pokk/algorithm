""" Created by Jieyi on 2/11/16. """
from data_structure.list.__interface__ import LinkedListNode


class TestObj:
    """
    Testing object.
    """

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return 'name: %s, age: %d, sex: %s' % (self.name, self.age, self.sex)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class LinkList:
    """
    Double linked list. All of the linked list operation.
    """

    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_node(self, obj):
        if self.__head is None:
            self.__head = LinkedListNode(obj)
            self.__tail = self.__head
        else:
            ptr = LinkedListNode(obj)
            self.__tail.next = ptr
            ptr.previous = self.__tail
            self.__tail = ptr

    def find(self, obj):
        node, index = self.__find_node_and_index(obj)
        return node.content

    def delete(self, obj):
        res, index = self.__find_node_and_index(obj)

        if res:
            prev = res.previous
            nex = res.next

            if prev is not None:
                prev.next = nex
            else:
                self.__head = res.next

            if nex is not None:
                nex.previous = prev

            del res
            return True
        else:
            print("we don't find it ><")
            return False

    def show_list(self):
        ptr = self.__head
        while ptr:
            print(ptr)
            ptr = ptr.next

    def __find_node_and_index(self, obj):
        ptr = self.__head
        index = 0

        while ptr:
            if obj == ptr.data:
                return ptr, index
            ptr = ptr.next
            index += 1

        return None


def main():
    n = LinkList()
    n.add_node(TestObj('Jieyi', 12, 'boy'))
    n.add_node(TestObj('Toby', 13, 'boy'))
    n.add_node(TestObj('Peter', 14, 'boy'))
    n.add_node(TestObj('John', 15, 'boy'))
    n.add_node(TestObj('Mary', 16, 'girl'))
    n.add_node(TestObj('Gary', 17, 'boy'))
    n.add_node(TestObj('Helen', 18, 'girl'))
    n.show_list()

    print('====================')

    n.delete(TestObj('Peter', 14, 'boy'))
    n.show_list()


if __name__ == '__main__':
    main()
