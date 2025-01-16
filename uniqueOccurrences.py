# pylint: skip-file

'''
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict, occurrences = dict(), set()
        for num in arr:
            if num in arr_dict:
                arr_dict[num] += 1
            else:
                arr_dict[num] = 1 
        for key, value in arr_dict.items():
            if value in occurrences:
                return False
            else:
                occurrences.add(value)
        return True


if __name__ == "__main__":
    arr = [1,2]
    print(f'arr: {arr}')
    solution = Solution()
    OUTPUT = solution.uniqueOccurrences(arr)
    print(f'uniqueOccurrences: {OUTPUT}')
    EXPECTED_OUTPUT = False
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')