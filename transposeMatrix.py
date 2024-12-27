'''transposeMatrix.py'''
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

Question:
# array of values
# find the minimum sum of values that cannot be created
# coins can not reused to make new value

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

Observations / Clarifying Questions / Insights:
- flip the row and index for each
- flip the rows and columns
- postive integers

Output: transposed matrix
-
'''

# O(w * h) time | O(w * h) space
def transposeMatrix(matrix):
    transposed_matrix = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed_matrix.append(new_row)
    return transposed_matrix


matrix = [
    [1]
]
print("matrix:", matrix)
print("transposeMatrix:", transposeMatrix(matrix))
print(" ")

matrix = [
    [1],
    [-1]
]
print("matrix:", matrix)
print("transposeMatrix:", transposeMatrix(matrix))
print(" ")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("matrix:", matrix)
print("transposeMatrix:", transposeMatrix(matrix))
print(" ")

# _recursion
# _iteration