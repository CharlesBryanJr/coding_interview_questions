# pylint: skip-file

'''
2390. Removing Stars From a String

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 
Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
'''

from typing import List

class Solution:
    def removeStars(self, s: str) -> str:
        star_count = 0
        for char in s:
            if char == '*':
                star_count += 1
        print(f'star_count: {star_count}')
        result, i = '', len(s) - 1
        while i >= 0:
            print(f'i: {i}')
            print(f's[{i}]: {s[i]}')
            print(f'star_count: {star_count}')
            print(f'result: {result}')
            print()
            if s[i] == '*':
                pass
            else:
                if star_count <= 0:
                    result += s[i]
                star_count -= 1
            i -= 1
        return result


if __name__ == "__main__":
    s = "leet**cod*e"
    print(f's: {s}')
    solution = Solution()
    OUTPUT = solution.removeStars(s)
    print(f'removeStars: {OUTPUT}')
    EXPECTED_OUTPUT = "lecoe"
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')