# pylint: skip-file

'''
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''

from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels, n = set('aeiou'), len(s)
        vowel_count = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels_count = vowel_count
        for i in range(k, n):
            if s[i-k] in vowels:
                vowel_count -= 1
            if s[i] in vowels:
                vowel_count += 1
            if vowel_count > max_vowels_count:
                max_vowels_count = vowel_count
            if max_vowels_count == k:
                return k
        return max_vowels_count


if __name__ == "__main__":
    s = 'abciiidef'
    k = 3
    print(f's: {s}')
    print(f'k: {k}')
    solution = Solution()
    OUTPUT = solution.maxVowels(s, k)
    print(f'maxVowels: {OUTPUT}')
    EXPECTED_OUTPUT = 3
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')