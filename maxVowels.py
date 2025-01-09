# pylint: skip-file

'''
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