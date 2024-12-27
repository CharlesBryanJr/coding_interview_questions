'''semordnilap.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- list of unique strings

return:
- a list of semordnilap pairs

notes:
- pair
- different strings
- reverse of one word is the same as the forward version of the other.
- order of strings does not matter

'''


def palindrome(words):
    semordnilap_pairs = []
    words_length = len(words)
    store_idxs = {}

    for current_idx in range(words_length):
        word = words[current_idx]
        word_length = len(word)

        for iterator in range(words_length):
            palindrome = words[iterator]
            palindrome_length = len(palindrome)

            if word_length == palindrome_length and current_idx != iterator:
                if word == palindrome[::-1]:
                    if current_idx not in store_idxs:
                        if iterator not in store_idxs:
                            semordnilap_pairs.append(tuple((word, palindrome)))
                            store_idxs[current_idx] = store_idxs.get(
                                current_idx, 0) + 1
                            store_idxs[iterator] = store_idxs.get(
                                iterator, 0) + 1

    return semordnilap_pairs


def semordnilap(words):
    semordnilap_pairs = []
    words_length = len(words)
    words_dict = {}

    for current_idx in range(words_length):
        word = words[current_idx]
        words_dict[word] = current_idx

    for current_idx in range(words_length):
        word = words[current_idx]
        palindrome = word[::-1]

        if palindrome in words_dict:
            palindrome_idx = words_dict[palindrome]

            if current_idx != palindrome_idx:
                semordnilap_pairs.append(tuple((word, palindrome)))
                words_dict.pop(word)

    return semordnilap_pairs


words1 = ["abcde", "edcba", "edbc", "edb", "cbde", "abc"]
print("words1:", words1)
print("palindrome:", palindrome(words1))
print("semordnilap:", semordnilap(words1))
print(" ")
words2 = ["aaa", "bbbb"]
print("words2:", words2)
print("palindrome:", palindrome(words2))
print("semordnilap:", semordnilap(words2))
print(" ")
words3 = ["dog", "god"]
print("words3", words3)
print("palindrome:", palindrome(words3))
print("semordnilap:", semordnilap(words3))
print(" ")

# _recursion
# _iteration
print(" ")
