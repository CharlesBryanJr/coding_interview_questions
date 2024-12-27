'''generateDocument.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

givens:
-a string of available characters
-a string of the document that needs to be generated

return boolen True if you can create the document using the available characters
return boolen False if you can not create the document using the avaiable characters

Note:
-if the frequency of unique characters matters
-all characters can be inside the input
-empty string can always be generated

'''


# Time: O(n + m) | # Space: O(n)
def generateDocument(characters, document):
    if document == "":
        return True

    available_chars = {}

    for char in characters:
        if char in available_chars:
            available_chars[char] += 1
        else:
            available_chars[char] = 1

    print(available_chars)

    for char in document:
        if char in available_chars:
            available_chars[char] -= 1
            if available_chars.get(char) < 0:
                return False
        else:
            print(available_chars)
            return False

    return True


characters1 = "Bste!hetsi ogEAxpelrt x "
document1 = "AlgoExpert is the Best!"
print(generateDocument(characters1, document1))
print(" ")
characters2 = "aheaolabbhb"
document2 = "hello"
print(generateDocument(characters2, document2))
print(" ")

# _recursion
# _iteration
print(" ")
