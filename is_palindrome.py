'''is_palindrome.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
given a non-empty string
determine if the string is a Palindrome
if so, returl boolean True
if not, return boolen False

Palindrome
-is string
-that is written forward and backwards the same
-single character strings are Palindromes
'''
# _recursion
# _iteration

# Time: O(n) | # Space: O(1)
def is_palindrome_iteration(string):

    if len(string) == 1:
        return True

    string_length = len(string)

    for fwd_idx in range(string_length):
        rev_idx = (string_length - 1) - fwd_idx

        if string[fwd_idx] != string[rev_idx]:
            print(f"string[{fwd_idx}]:",string[fwd_idx])
            print(f"string[{rev_idx}]:",string[rev_idx])
            return False

    return True

def is_palindrome__recursion(string, fwd_idx=0, rev_idx=0):
    if fwd_idx >= len(string) - 1:
        return None

    string_length = len(string)

    if string_length == 1:
        return True

    if fwd_idx == 0:
        rev_idx = string_length - 1

    if string[fwd_idx] == string[rev_idx]:
        is_palindrome__recursion(string, fwd_idx + 1, rev_idx - 1)
    else:
        print("string[fwd_idx]:",string[fwd_idx])
        print("string[rev_idx]:",string[rev_idx])
        return False

    return True


string1 = "abcdcba"
string2 = "a"
string3 = "ab"
string4 = "aba"
string5 = "abcdefghihgfeddcba"
print(F"{string1}, isPalindrome:",is_palindrome_iteration(string1))
print(F"{string1}, isPalindrome:",is_palindrome__recursion(string1))
print(" ")
print(F"{string2}, isPalindrome:",is_palindrome_iteration(string2))
print(F"{string2}, isPalindrome:",is_palindrome__recursion(string2))
print(" ")
print(F"{string3}, isPalindrome:",is_palindrome_iteration(string3))
print(F"{string3}, isPalindrome:",is_palindrome__recursion(string3))
print(" ")
print(F"{string4}, isPalindrome:",is_palindrome_iteration(string4))
print(F"{string4}, isPalindrome:",is_palindrome__recursion(string4))
print(" ")
print(F"{string5}, isPalindrome:",is_palindrome_iteration(string5))
print(F"{string5}, isPalindrome:",is_palindrome__recursion(string5))
print(" ")