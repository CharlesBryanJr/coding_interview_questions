'''levenshteinDistance.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- two strings

action:
-
return:
- minimum number of edit operations to transform the first string into the second string

note:
- insert a char
- delete a char
- substitution of a char to another char 


'''

# Time: O(nm) | # Space: O(nm)


def levenshteinDistance(str1, str2):
    pass


str1 = "abc"
str2 = "yabd"
print("str1:", str1)
print("str2:", str2)
print("levenshteinDistance:", levenshteinDistance(str1, str2))
print(" ")

str1 = "cereal"
str2 = "saturday"
print("str1:", str1)
print("str2:", str2)
print("levenshteinDistance:", levenshteinDistance(str1, str2))
print(" ")

str1 = "abcdefghij"
str2 = "1234567890"
print("str1:", str1)
print("str2:", str2)
print("levenshteinDistance:", levenshteinDistance(str1, str2))
print(" ")

# _recursion
# _iteration
print(" ")
