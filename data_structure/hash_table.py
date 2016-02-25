""" Created by Jieyi on 2/11/16. """


class TestObject:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self):
        return 'a: %s, b: %d, c: %s' % (self.__a, self.__b, self.__c)


class HashTable:
    def __init__(self):
        self.__div_group = 10
        self.__hash_table = []
        # Init the 2-dim array.
        for i in range(self.__div_group):
            self.__hash_table.append([])

    def __str__(self):
        index = 0

        for l_1 in self.__hash_table:
            if len(l_1) is 0:
                index += 1
                continue

            index_y = 0
            for l_2 in l_1:
                index_y += 1
                print(index, ',', index_y, ' ->', l_2)

            index += 1
        return ''

    def hash(self, obj):
        val = self.__cal_value(obj)
        self.__hash_table[val].append(obj)

    def find(self, obj):
        val = self.__cal_value(obj)
        for o in self.__hash_table[val]:
            if o is obj:
                print('We find it!!')
                return True

        print('What a shame! >_<')
        return False

    def delete(self, obj):
        index = 0
        val = self.__cal_value(obj)
        for o in self.__hash_table[val]:
            if o is obj:
                del self.__hash_table[val][index]
                return True
            index += 1
        return False

    def __cal_value(self, obj):
        total = 0
        for v in obj.__dict__:
            # Get the first of string character ASCII.
            if type(obj.__dict__[v]) is str:
                total += ord(obj.__dict__[v][0])
            elif type(obj.__dict__[v]) is int:
                total += obj.__dict__[v]

        return total % self.__div_group


def main():
    h = HashTable()
    a = TestObject("Wu", 30, "Taiwan")
    b = TestObject("Jieyi", 23, "taiwan")
    c = TestObject("Mariko", 18, "Japan")

    h.hash(a)
    h.hash(b)
    h.hash(c)

    h.find(c)

    print(h)


if __name__ == '__main__':
    main()
