'''caesar_cipher_encryptor.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
given
-a non empty string of lowercase characters
and
-a non negative integer represeting a key

return a new string
-shift every character "k" postions

note:
characters should wrap if they pass z
'''

# Time: O(n) | # Space: O(n)


def caesarCipherEncryptor(string, key):
    shifted_string = ''
    first_char_Unicode = ord("a")
    last_char_Unicode = ord("z")
    key = key % 26
    wrap_char = last_char_Unicode - first_char_Unicode + 1

    for char in string:
        if ord(char) + key > last_char_Unicode:
            shifted_char = ord(char) + key - wrap_char
            shifted_string += chr(shifted_char)
        else:
            shifted_char = ord(char) + key
            shifted_string += chr(shifted_char)

    return shifted_string


string1 = "xyz"
key1 = 2
print(F"String1: {string1}")
print(F"key1: {key1}")
print("after:", caesarCipherEncryptor(string1, key1))
print(" ")
string2 = "abc"
key2 = 0
print(F"String2: {string2}")
print(F"key2: {key2}")
print("after:", caesarCipherEncryptor(string2, key2))
print(" ")
string3 = "abc"
key3 = 3
print(F"string3: {string3}")
print(F"key3: {key1}")
print("after:", caesarCipherEncryptor(string3, key3))
print(" ")
