'''
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Helper function to compute GCD of two integers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # If str1 + str2 != str2 + str1, there's no common divisor string
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # The GCD string is the prefix of length gcd_length in either string
        return str1[:gcd_length]