'''run_length_encoding.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
given:
non empty string

return the given string's run length encoding

Note:
-special characters
-numbers

Ex1. AAA ---> 3A
Ex2. AAAAAAAAAAAA ---> 9A93
'''

# Time: O(n) | # Space: O(n)


def runLengthEncoding(string):
    string_length = len(string)
    encoded_string = ""
    current_char_count = 1

    for idx in range(1, string_length):
        current_char = string[idx]
        last_char = string[idx - 1]

        if current_char != last_char or current_char_count == 9:
            encoded_string += str(current_char_count)
            encoded_string += last_char
            current_char_count = 0

        current_char_count += 1

    encoded_string += str(current_char_count)
    encoded_string += string[string_length-1]

    return encoded_string


string1 = "AAAAAAAAAAAAABBCCCCDD"
string2 = "aA"
string3 = "122333"
string4 = "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"

print("string1:", string1)
print(runLengthEncoding(string1))
print(" ")
print("string2:", string2)
print(runLengthEncoding(string2))
print(" ")
print("string3:", string3)
print(runLengthEncoding(string3))
print(" ")
print("string4:", string4)
print(runLengthEncoding(string4))
print(" ")


# _recursion
# _iteration
print(" ")
