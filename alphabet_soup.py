'''alphabet_soup.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

input1 = "hello"
input2 = "eLEPhAnt"


def alphabet_soup(string_input, part):

    length_of_input = len(string_input)
    result = ""
    lowest_char = string_input[0]

    if part.upper() == "A":
        while len(result) < length_of_input:

            if len(string_input) > 0:
                lowest_char = string_input[0]

            for char in string_input:
                if char < lowest_char:
                    lowest_char = char

            result += lowest_char

            input_updated = ""
            found_lowest_char = False
            for char in string_input:

                if not char == lowest_char:
                    input_updated += char

                if char == lowest_char and found_lowest_char:
                    input_updated += char

                if char == lowest_char and not found_lowest_char:
                    found_lowest_char = True

            string_input = input_updated

    if part.upper() == "B":
        while len(result) < length_of_input:

            if len(string_input) > 0:
                lowest_char = string_input[0]

            for char in string_input:

                if lowest_char.upper() == char:
                    lowest_char = char

                uppercase_char = char.upper()
                uppercase_lowest_char = lowest_char.upper()

                if uppercase_char < uppercase_lowest_char:
                    lowest_char = char

            result += lowest_char

            input_updated = ""
            found_lowest_char = False
            for char in string_input:

                if not char == lowest_char:
                    input_updated += char

                if char == lowest_char and found_lowest_char:
                    input_updated += char

                if char == lowest_char and not found_lowest_char:
                    found_lowest_char = True

            string_input = input_updated

    return result

print(alphabet_soup(input1, "A"))
print(" ")
print(" ")
print(alphabet_soup(input2, "B"))

print(" ")
