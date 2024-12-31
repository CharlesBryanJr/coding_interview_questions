'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ("a", "e", "i", "o", "u")
        found_vowels = []
        found_vowels_index = []
        res_array = list(s)

        for i in range(len(s)):
            if s[i].lower() in vowels:
                found_vowels.append(s[i])
                found_vowels_index.append(i)
       
        l, r = 0, len(found_vowels_index) - 1
        while l < r:
            res_array[found_vowels_index[l]] = found_vowels[r]
            res_array[found_vowels_index[r]] = found_vowels[l]
            l += 1
            r -= 1

        return "".join(res_array)


if __name__ == "__main__":
    s = "IceCreAm"
    print(f's: {s}')
    solution = Solution()
    print(f'canPlaceFlowers: {solution.reverseVowels(s)}')