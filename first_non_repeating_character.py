'''first_non_repeating_character.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
given:
- a string of lowercase english characters

return:
- the index of the given string's first non repeating character

goal:
-find the first character in the string that occurs only once

note:
- return -1 if the given string does not have any non repeating characters

'''

# Time: O(n) | # Space: O(1)
def firstNonRepeatingCharacter(string):
    string_length = len(string)
    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    for idx in range(string_length):
        char = string[idx]

        if char_count[char] == 1:
            return idx

    return -1

# _recursion
# _iteration


string1 = "abcdcaf"
string2 = "faadabcbbebdf"
string3 = "ababac"
string4 = "a"
string5 = ""
print("string1:", string1)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string1))
print(" ")
print("string2:", string2)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string2))
print(" ")
print("string3:", string3)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string3))
print(" ")
print("string4:", string4)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string4))
print(" ")
print("string5:", string5)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string5))
print(" ")
