# pylint: skip-file

'''
443. String Compression
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''


from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read, n = 0, 0, len(chars)
        while read < n:
            start = read
            chars[write] = chars[start]
            write += 1
            while read < n and chars[read] == chars[start]:
                read += 1
            length = read - start
            if length > 1:
                for digit in str(length):
                    chars[write] = digit
                    write += 1
        return write


if __name__ == "__main__":
    chars = ["a","a","a","a","b","a"]
    print(f'chars: {chars}')
    solution = Solution()
    OUTPUT = solution.compress(chars)
    print(f'compress: {OUTPUT}')
    EXPECTED_OUTPUT = ["a","4","b","a"]
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'Expected Output Count: {len(EXPECTED_OUTPUT)}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == len(EXPECTED_OUTPUT)}')