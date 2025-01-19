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
        result = ''
        print(f"Initial string: {s}")
        i = len(s) - 1
        
        while i >= 0:
            print(f"\nTop of outer loop, i = {i}")
            
            # Process non-star characters
            while i >= 0 and s[i] != '*':
                print(f"Adding s[{i}] = '{s[i]}' to result.")
                result += s[i]
                i -= 1
            
            print(f"Finished non-star sequence, i = {i}, result so far = '{result}'")
            
            # Count stars
            star_count = 0
            while i >= 0 and s[i] == '*':
                print(f"Found '*' at s[{i}].")
                star_count += 1
                i -= 1
            
            print(f"Counted {star_count} stars, now i = {i}")
            
            # Skip characters based on star_count
            if i >= 0:
                print(f"Before skipping characters, i = {i}, star_count = {star_count}")
                i -= star_count
                print(f"After skipping characters, i = {i}")
                
                # Check if next index is valid for printing
                if i >= 0:
                    print(f"Next character to process: s[{i}] = '{s[i]}'")
                else:
                    print("i is less than 0, no next character to process.")
        
        print(f"\nFinal reversed result before reversing: '{result}'")
        final_result = result[::-1]
        print(f"Final result after reversing: '{final_result}'")
        return final_result


if __name__ == "__main__":
    s = "abb*cdfg*****x*"
    print(f's: {s}')
    solution = Solution()
    OUTPUT = solution.removeStars(s)
    print(f'removeStars: {OUTPUT}')
    EXPECTED_OUTPUT = "lecoe"
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')