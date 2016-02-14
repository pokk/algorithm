""" Created by Jieyi on 2/11/16. """


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
    All of the linked list operation.
    """

    class _Node:
        """
        Linked list's node.
        """

        def __init__(self, obj):
            self.previous = None
            self.content = obj
            self.next = None

        def __str__(self):
            return str(self.content)

    def __init__(self):
        self.__list = None

    def add_node(self, obj):
        if self.__list is None:
            self.__list = self._Node(obj)
        else:
            ll = self.__list
            while ll.next:
                ll = ll.next
            new_ll = self._Node(obj)
            ll.next = new_ll
            new_ll.previous = ll

    def find_node(self, obj):
        ll = self.__list
        index = 0

        while ll:
            if obj == ll.content:
                return ll, index
            ll = ll.next
            index += 1

        return None

    def del_node(self, obj):
        res, index = self.find_node(obj)

        if res:
            prev = res.previous
            nex = res.next

            if prev is not None:
                prev.next = nex
            else:
                self.__list = res.next

            if nex is not None:
                nex.previous = prev

            del res
        else:
            print("we don't find it ><")

    def show_list(self):
        ll = self.__list
        while ll:
            print(ll)
            ll = ll.next


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

    n.del_node(TestObj('Peter', 14, 'boy'))
    n.show_list()


if __name__ == '__main__':
    main()
