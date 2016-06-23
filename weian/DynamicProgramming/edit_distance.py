#!/usr/bin/python


def ed_table(string1, string2):
    result = [[0 for _ in range(len(string1))] for _ in range(len(string2))]

    for i in range(len(string2)):
        for j in range(len(string1)):
            if i == 0:
                print("i=" + str(i) + " j=" + str(j))
                result[0][j] = j
                continue

            if j == 0:
                result[i][0] = i
                continue

            if string1[j] == string2[i]:
                result[i][j] = result[i-1][j-1]
                continue

            result[i][j] = 1 + min(result[i-1][j], result[i][j-1], result[
                i-1][j-1])

    print(result)
    return result[len(string2)-1][len(string1)-1]


def levenshtein(string1, string2, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if string1[m-1] == string2[n-1]:
        cost = 0
    else:
        cost = 1

    return min(levenshtein(string1, string2, m-1, n) + 1, levenshtein(
        string1, string2, m, n-1) + 1, levenshtein(string1, string2, m-1,
                                                   n-1) + cost)


def edit_distance_recursive(string1, string2, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if string1[m-1] == string2[n-1]:
        return edit_distance_recursive(string1, string2, m-1, n-1)

    return 1 + min(edit_distance_recursive(string1, string2, m, n-1),
                   edit_distance_recursive(string1, string2, m-1, n),
                   edit_distance_recursive(string1, string2, m-1, n-1))


def main():
    str1 = "geek"
    str2 = "gesek"
    print(edit_distance_recursive(str1, str2, len(str1), len(str2)))
    print(levenshtein(str1, str2, len(str1), len(str2)))
    print(ed_table(str1, str2))

if __name__ == '__main__':
    main()
