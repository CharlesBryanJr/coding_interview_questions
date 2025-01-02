'''
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

class Solution:
    def reverseWords(self, s: str) -> str:
        print(f"Original string: '{s}'")
        
        # Step 1: Strip leading/trailing spaces
        stripped_s = s.strip()
        print(f"After stripping: '{stripped_s}'")
        
        # Step 2: Split on whitespace
        words = stripped_s.split()
        print(f"Split words: {words}")
        
        # Step 3: Reverse the list of words
        words.reverse()
        print(f"Reversed words: {words}")
        
        # Step 4: Join the reversed words with a single space
        result = " ".join(words)
        print(f"Final reversed string: '{result}'")
        
        return result
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word = []
        word_complete = False
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                word_complete = True
            else:
                word.append(s[i])
                word_complete = False
            if word_complete and len(word) > 0:
                for j in reversed(range(len(word))):
                    res.append(word[j])
                res.append(" ")
                word = []
            i -= 1
        if len(word) > 0:
            for j in reversed(range(len(word))):
                res.append(word[j])
        if res and res[-1] == ' ':
            res.pop()
        return "".join(res)


if __name__ == "__main__":
    s = "  hello world  "
    print(f's: {s}')
    solution = Solution()
    print(f'reverseWords: {solution.reverseWords(s)}')