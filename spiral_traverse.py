'''spiral_traverse.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
print(" ")

'''

given:
-  a two dimensional array n by m


Type of Question:
- Array
	- draw indices
	- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values
	- running sums
	- sliding windows
		- start_of_window
		- end_of_window

- Recursion
	- the solution depends on solutions to smaller instances of the same problem
		- define the smaller instance of the problem
	- will iterate/traverse until the function can return a value (base case)
		- always include return statment
	- to keep track of element, store the element in a variable that connected to the recursion call
	- running variables can be passed as arguments
	- Recursive functions often take a sub array of the original array
	- the outcome of a recursive function will affect code on lines after it
	- To optimize use memoization
		- store the answer to recursive calls in a hash table

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Arrays
			- Empty array
			- Nested or not nested

Observations / Clarifying Questions / Insights:
- if n == m, the given array is a square
- spiral order starts at the top left corner of the array

- simplest / smallest problem
	- traversing the perimeter

return:
- return a one dimensional array in spiral order
'''

'''
# Time: O(n) | # Space: O(n)
Iteration Main Function

Input(array): array

create an empty output array
    # to store the array values in spiral order
    - spiral_array = []

create pointers and initalize at orginal locations
    # these four pointer will be used to traverse the array
    - start_row = 0
    - end_row = len(array) - 1
    - start_column = 0
    - end_column = len(array[0]) - 1

traverse the perimeter of the array
    # when the both set of pointers cross
        # the entire array has been traversed
        # So, the loop should continue until then
    - while the start_row <= end_row and start_column <= end_column:

    traverse the first row and append each num to the output array
        - traverse_right(array, spiral_array, start, end)

    traverse the last column and append each num to the output array
        - traverse_down(array, spiral_array, start, end)

    traverse the last row and append each num to the output array
        - traverse_left(array, spiral_array, start, end)

    traverse the first column and append each num to the output array
        - traverse_up(array, spiral_array, start, end)

    update pointers to for the next iteration
        # to traverse the inner matrix, we need to update the pointers
        # our pointers will dicate the where the functions traverse in the array
        - start_row += 1
        - end_row -= 1
        - start_column += 1
        - end_column -= 1

Output(array): spiral_array
	# a one dimensional array in spiral order
'''

# Time: O(n) | # Space: O(n)
def spiral_traverse_iteration(array):
    result = []
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1

    while start_col <= end_col and start_row <= end_row:
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(array[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result


'''
# Time: O(n) | # Space: O(n)
Recursion Main Function

Input(array): array

create an empty output array
    # to store the array values in spiral order
    - spiral_array = []

create pointers and initalize at orginal locations
    # these four pointer will be used to traverse the array
    - start_row = 0
    - end_row = len(array) - 1
    - start_column = 0
    - end_column = len(array[0]) - 1

call the recursion helper function
    # will solve smaller instances of the same problem
    # iterate/traverse until the function can return a value
        # iterate/traverse until the base case 
    - spiral_traverse(array, start_row, end_row, start_column, end_colum, spiral_array)

Output(array): spiral_array
	# a one dimensional array in spiral order
'''

'''
Recursion Helper Function

Input(array, int, int, int, int, array): array, start_row, end_row, start_column, end_column, spiral_array

define a base case so that the recursive function stops iterating
    # when the both set of pointers cross
        # the entire array has been traversed
        # So, the loop should continue until then
    - if start_row > end_row or start_column > end_column:

traverse the perimeter of the array

    traverse the first row and append each num to the output array
        - traverse_right(array, spiral_array, start, end)

    traverse the last column and append each num to the output array
        - traverse_down(array, spiral_array, start, end)

    traverse the last row and append each num to the output array
        - traverse_left(array, spiral_array, start, end)

    traverse the first column and append each num to the output array
        - traverse_up(array, spiral_array, start, end)

    update pointers to for the next iteration
        # to traverse the inner matrix, we need to update the pointers
        # our pointers will dicate the where the functions traverse in the array
        - start_row += 1
        - end_row -= 1
        - start_column += 1
        - end_column -= 1

    call the recursion helper function
    # will solve smaller instances of the same problem
    # iterate/traverse until the function can return a value
        # iterate/traverse until the base case 
    - spiral_traverse(array, start_row, end_row, start_col, end_col, spiral_array)
'''

# Time: O(n) | # Space: O(n)
def spiral_traverse_recursion(array):
    result = []
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1
    spiral_traverse(array, start_row, end_row, start_col, end_col, result)
    return result


def spiral_traverse(array, start_row, end_row, start_col, end_col, result):
    if start_row > end_row or start_col > end_col:
        return
    traverse_right(array, start_col, end_col + 1, start_row, result)
    traverse_down(array, start_row + 1, end_row + 1, end_col, result)
    if start_row != end_row:
        traverse_left(array, start_col, end_col - 1, end_row, result)
    if start_col != end_col:
        traverse_up(array, start_row + 1, end_row, start_col, result)
    return spiral_traverse(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, result)


def traverse_right(array, col, end_col, row, result):
    if col >= end_col:
        return
    result.append(array[row][col])
    return traverse_right(array, col + 1, end_col, row, result)

def traverse_down(array, row, end_row, col, result):
    if row >= end_row:
        return
    result.append(array[row][col])
    return traverse_down(array, row + 1, end_row, col, result)

def traverse_left(array, start_col, col, row, result):
    if col <= start_col:
        return
    result.append(array[row][col])
    return traverse_left(array, start_col, col - 1, row, result)

def traverse_up(array, start_row, row, col, result):
    if row < start_row:
        return
    result.append(array[row][col])
    return traverse_up(array, start_row, row - 1, col, result)


array = [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10, 9, 8, 7]]
print("array:", array)
print("spiral_traverse_iteration:", spiral_traverse_iteration(array))
print("spiral_traverse_recursion:", spiral_traverse_recursion(array))
print(" ")

array = [[27, 12, 35, 26],
         [25, 21, 94, 11],
         [19, 96, 43, 56],
         [55, 36, 10, 18],
         [96, 83, 31, 94],
         [93, 11, 90, 16]]
print("array:", array)
print("spiral_traverse_iteration:", spiral_traverse_iteration(array))
print("spiral_traverse_recursion:", spiral_traverse_recursion(array))
print(" ")

array = [[1, 2, 3, 4],
         [10, 11, 12, 5],
         [9, 8, 7, 6]]
print("array:", array)
print("spiral_traverse_iteration:", spiral_traverse_iteration(array))
print("spiral_traverse_recursion:", spiral_traverse_recursion(array))
print(" ")
