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

        # If lengths are different, they can't be close
        # Count frequency of each character in both words
        # Check if both have the same set of unique characters
        # Sort the frequency counts
        # Check if the sorted frequency lists are equal



from typing import List


from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_values_and_count, word2_values_and_count = Counter(word1), Counter(word2)
        if word1_values_and_count.keys() != word2_values_and_count.keys():
            return False
        word1_sorted_value_counts = sorted(word1_values_and_count.values())
        word2_sorted_value_counts = sorted(word2_values_and_count.values())
        if word1_sorted_value_counts != word2_sorted_value_counts:
            return False
        return True


if __name__ == "__main__":
    word1 = "cabbba"
    word2 = "abbccc"
    print(f'word1: {word1}')
    print(f'word2: {word2}')
    solution = Solution()
    OUTPUT = solution.closeStrings(word1, word2)
    print(f'closeStrings: {OUTPUT}')
    EXPECTED_OUTPUT = True
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')