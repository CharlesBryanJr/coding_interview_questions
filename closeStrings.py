# pylint: skip-file

'''
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
'''

from typing import List


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        updated_word1 = [char for char in word1]
        n = len(word1)
        indexes_with_incorrect_chars = list()
        word1_dict, word2_dict = dict(), dict()
        for i in range(n):
            if word1[i] != word2[i]:
                indexes_with_incorrect_chars.append(i)
            word1_dict[word1[i]] = i
            word2_dict[word2[i]] = i
        if len(indexes_with_incorrect_chars) == 0:
            return True
        print(f'indexes_with_incorrect_chars: {indexes_with_incorrect_chars}')
        print(f'word1_dict: {word1_dict}')
        print(f'word2_dict: {word2_dict}')
        for index in indexes_with_incorrect_chars:
            what_char_is = word1[index]
            what_char_should_be = word2[index]
            what_char_should_be_idx = word1_dict[what_char_should_be]
            print(f'index: {index}')
            print(f'what_char_is: {what_char_is}')
            print(f'what_char_should_be: {what_char_should_be}')
            print(f'what_char_should_be_idx: {what_char_should_be_idx}')
            print(f'updated_word1: {updated_word1}')
            updated_word1[index] = what_char_should_be
            updated_word1[what_char_should_be_idx] = what_char_is
            print(f'updated_word1: {updated_word1}')
            print()

        return True if updated_word1 == word2 else False


if __name__ == "__main__":
    word1 = "abc"
    word2 = "bca"
    print(f'word1: {word1}')
    print(f'word2: {word2}')
    solution = Solution()
    OUTPUT = solution.closeStrings(word1, word2)
    print(f'closeStrings: {OUTPUT}')
    EXPECTED_OUTPUT = True
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')