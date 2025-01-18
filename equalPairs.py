# pylint: skip-file

'''
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 
Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
'''



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