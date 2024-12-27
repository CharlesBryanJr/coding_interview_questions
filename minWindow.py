
'''

Given
two
strings
s and t
of
lengths
m and n
respectively,
return the
minimum
window
substring
of
s
such
that
every
character in t(including
duplicates) is included in the
window.If
there is no
such
substring,
return the
empty
string
"".

The
testcases
will
be
generated
such
that
the
answer is unique.
'''

class Solution(object):
    def minWindow(self, s, t):
        # Initialize a dictionary to track required characters and their counts
        required_chars = {}
        for char in t:
            required_chars[char] = required_chars.get(char, 0) + 1

        # Initialize a count for missing required characters
        missing_chars_count = len(t)

        # Initialize pointers for the current window
        left = start = end = 0

        # Iterate through the string 's' using a right pointer
        for right, current_char in enumerate(s, 1):

            # Decrement the count of 'current_char' in the required characters dictionary
            if current_char in required_chars and required_chars[current_char] > 0:
                missing_chars_count -= 1
            if current_char in required_chars:
                required_chars[current_char] -= 1

            # When all required characters are found, minimize the window
            if missing_chars_count == 0:
                while left < right and (
                        # Move the left pointer to the right while conditions are met
                        s[left] not in required_chars or required_chars[s[left]] < 0):

                    if s[left] in required_chars:
                        # Increment the count of characters as they move out of the window
                        required_chars[s[left]] += 1
                    left += 1

                # Update the minimum window indices if a smaller window is found
                if end == 0 or right - left <= end - start:
                    start, end = left, right

        # Return the minimum window substring
        return s[start:end]


s = "ADOBECODEBANC"
t = "ABC"

print(minRewards(s,t))

'''
Now, let's iterate through the string **`s`**:

1. We start with the right pointer at index 1 (character 'D').
2. 'D' is not in **`t`**, so we continue.
3. Right pointer at index 2 (character 'O').
4. 'O' is not in **`t`**, so we continue.
5. Right pointer at index 3 (character 'B').
6. 'B' is in **`t`**, so we decrement its count in **`required_chars`** and update **`missing_chars_count`** to 2.
7. Right pointer at index 4 (character 'E').
8. 'E' is not in **`t`**, so we continue.
9. Right pointer at index 5 (character 'C').
10. 'C' is in **`t`**, so we decrement its count in **`required_chars`** and update **`missing_chars_count`** to 1.

At this point, we have found all required characters at least once (missing_chars_count == 0). Now, we minimize the window by moving the left pointer:

1. Left pointer at index 0 (character 'A').
2. 'A' is in **`t`**, so we decrement its count in **`required_chars`** and update **`missing_chars_count`** to 0.
3. The left pointer moves to index 1 (character 'D').

We continue this process:

1. Right pointer at index 6 (character 'O').
2. Right pointer at index 7 (character 'D').
3. Right pointer at index 8 (character 'E').

Now, we minimize the window further:

1. Left pointer at index 2 (character 'O').
2. Left pointer at index 3 (character 'B').

The minimum window size is currently "BECODEBA," but it can't be minimized further.

1. Right pointer at index 9 (character 'B').
2. Right pointer at index 10 (character 'A').

Now, we minimize the window again:

1. Left pointer at index 4 (character 'E').
2. Left pointer at index 5 (character 'C').

The minimum window size is now "CODEBA."

1. Right pointer at index 11 (character 'N').

Now, we minimize the window again:

1. Left pointer at index 6 (character 'O').
2. Left pointer at index 7 (character 'D').
3. Left pointer at index 8 (character 'E').

The minimum window size is now "BANC."

Finally, we return the minimum window substring:

Output: BANC
'''