#!/usr/bin/python3

def lcs(str1, str2):
	len1 = len(str1)
	len2 = len(str2)

	result_table = [[ 0 for i in xrange(len1) ] for j in xrange(len2) ]

	for i in range(len1):
		for j in range(len2):
			if i == 0 and j == 0 and str1[i] == str2[j]:
				result_table[i][j] = 1
			elif str1[i - 1] == str2[j - 1]:
				result_table[i][j] = result_table[i - 1][j - 1] + 1
			else:
				result_table[i][j] = max(result_table[i - 1][j], result_table[i][j - 1])

	return result_table[len1 - 1][len2 - 1]

def main():
	str1 = "ABCDGH"
	str2 = "AEDFHR"

	print("len: " + str(lcs(str1, str2)))

if __name__ == '__main__':
	main()