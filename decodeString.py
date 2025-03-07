# pylint: skip-file

'''
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

from typing import List
from typing import Tuple

        
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack, str_stack = [], []
        current_num, current_str = 0, ''        
        for char in s:
            print(f"Before processing: current_num = {current_num}, current_str = '{current_str}', num_stack = {num_stack}, str_stack = {str_stack}")
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num, current_str= 0, ''
            elif char == ']':
                num = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
            print(f"After processing: current_num = {current_num}, current_str = '{current_str}', num_stack = {num_stack}, str_stack = {str_stack}\n")
        return current_str


if __name__ == "__main__":
    s = "2[abc]3[cd]ef"
    print(f's: {s}')
    solution = Solution()
    OUTPUT = solution.decodeString(s)
    print(f'decodeString: {OUTPUT}')
    EXPECTED_OUTPUT = "abcabccdcdcdef"
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')