#include <iostream>
#include <vector>    // std::vector()
#include <algorithm> // std::max()
#include <cstring>   // strlen()

/* making a table to record the result of matching. */
int LCS(const char *str1, const char *str2,
           const size_t len1, const size_t len2) {
    std::vector< std::vector<int> > result_array;

    // making a fix size of table.
    result_array.resize(len1);
    for(int i = 0 ; i < len1 ; i++) {
        result_array[i].resize(len2);
    }

    // initial the table, each component would be filled 0.
    for(int i = 0 ; i < len1 ; i++) {
        for(int j = 0 ; j < len2 ; j++) {
            result_array[i][j] = 0;
        }
    }

    // scanning the both of strings.
    for(int i = 0 ; i < len1 ; i++) {
        for(int j = 0 ; j < len2 ; j++) {
            if(i == 0 && j == 0 && str1[i] == str2[j]) {
                result_array[0][0] = 1;
            } else if(str1[i] == str2[j]) {
                if(i == 0 || j == 0)
                    result_array[i][j] = 1;
                else
                    result_array[i][j] = result_array[i-1][j-1] + 1;
            } else {
                if(i == 0 || j == 0) {
                    result_array[i][j] = std::max(result_array[0][j],
                                                  result_array[i][0]);
                } else
                    result_array[i][j] = std::max(result_array[i-1][j],
                                                  result_array[i][j-1]);
            }
        }
    }

    return result_array[len1 - 1][len2 - 1];
}

int main() {
    char str1[] = "ABCDGH";
    char str2[] = "AEDFHR";
    int len = LCS(str1, str2, strlen(str1), strlen(str2));

    std::cout << "LCS length is " << len << std::endl;

    return 0;
}