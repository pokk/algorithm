""" Created by wu.jieyi on 2016/02/24. """


def pascal(power):
    def formula(coefficient):
        """
        Add the 'a' and 'b' variable.

        :param coefficient: pascal coefficient array.
        """

        res_beautify = []
        for index in range(len(coefficient)):
            res_formula = ''
            if coefficient[index] is not 1:
                res_formula += str(coefficient[index])
            if len(coefficient) - index - 1 is not 0:
                res_formula += 'a^%d' % (len(coefficient) - index - 1)
            if index is not 0:
                res_formula += 'b^%d' % index
            res_beautify.append(res_formula)
        return ' + '.join(res_beautify)

    if power is 0:
        pascal_arr = [1]
    elif power is 1:
        pascal_arr = [1, 1]
    else:
        pascal_arr = [1, 1]
        for i in range(1, power):
            pascal_arr = [pascal_arr[j] + pascal_arr[j + 1] for j in range(len(pascal_arr) - 1)]
            pascal_arr[0:0] = [1]
            pascal_arr.append(1)
    # print(pascal_arr)
    return formula(pascal_arr)


def main():
    print(pascal(10))


if __name__ == '__main__':
    main()
