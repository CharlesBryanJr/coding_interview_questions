'''minimumPassesOfMatrix'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")

'''

Question:
-

Type of Question:
- Array
    multiple pointers
    sorting array
    mutating the current index or later index to count
    hash function the input
    	turn a index's value negative to keep track of duplicates

- Graphs
	- traverse through the graph DFS or BFS
			- for NON connected graphs, loop over every node
			- create and use a visited DS to optimize
	- trie edge == leads to a new descendant node
		- create a visited DS and initalize with false
	- back edge == leads to an already discovered ancestor node
		- if a back edge is exists == cycle
		- if a node is on the recursion stack and we reach it again
		- if a node is on the recursion stack, it is the ancestor of the current node
		- create a in_stack DS and initalize with false
	- cross edge == leads from one descendant to another already discovered descendant in a different subtree
	- forward edge == leads to an already discovered descendant node

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


Clarifying Questions / Insights:
- if one or more of its adjacent elements is postive, convert a negative integer to postive integer
    - multiply the negative integer by -1
- adjacent elements == top, left, right, bottom
- 0 is neither postive or negative
    - 0 can not help convert a negative number
    - 0 does not need to be converted
- single "pass" over the matrix == converting all the negative integers that CAN be converted at that time
- all updates have to be made after each "pass"
- since an action can only occur if we find a postive number, then that is the only thing we care about



- simplest / smallest problem
	-

- If I knew / had this....
	- if I found a negative num that I could not update, return -1
    - if I knew the location of all of the postive numbers during each iteration
        - i could just flip their neighbors
        - repeat


Output: integer
- the minimum number of "passes" required to conver all negative integers in the matrix to postive integers.
- if all the negative integers can not be converted, return -1
'''

'''
# Time: O(n) | # Space: O(n)
Main Function
Find all of the locations of postive integers in the matrix
    - Create a DS, queue, to store the locations of postive integers in the matrix

Store the locations of postive integers in the matrix
    - loop over the matrix and
        - if the num > 0
            - store it queue

For each the postive integers locations in the first queue, turn their negative neighbors postive
For every negative turned postive, I need to add that location to the second queue
    - pop postive integers locations out of the first queue
    - turn their negative neighbors postive
    - add their now postive neighbors to the second queue

For each the postive integers locations in the second queue, turn their negative neighbors postive
For every negative turned postive, I need to add that location to the first queue
    - pop postive integers locations out of the second queue
    - turn their negative neighbors postive
    - add their now postive neighbors to the first queue

Determine if any negative numbers still remain
    - loop over the matrix
        - if the num < 0,
            - return -1

For every negative

    - Input: matrix
        - create queue DS
        - loop over the entire matrix
            - if num >= 0
                - append the num_idx to queue

        - pop each postive integer location off of the first queue
            - run update_neighbors(idx, matrix)
                - add updated neighbors idx to second queue
            - increment minimum_number += 1

        - pop each postive integer location off of the second queue
            - run update_neighbors(idx, matrix)
                - add updated neighbors idx to first queue
            - increment minimum_number += 1

        - loop over the entire matrix
            - if num < 0
                - return -1

    - Output: integer
            - minimum_number
            - return -1, if all the negative integers can not be converted
# Time: O(n) | # Space: O(n)
def minimumPassesOfMatrix(matrix):
    minimum_passes = convert_negatives(matrix)
    if not contains_negative(matrix):
        return minimum_passes - 1
    else:
        return -1

def convert_negatives(matrix):
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])
    indices_to_update = []

    for row in range(num_of_rows):
        for col in range(num_of_cols):
            idx = (row, col)
            num = matrix[row][col]
            if idx in indices_to_update:
                continue
            if num < 0:
                continue

            neighbors = get_neighbors(idx, matrix)
            indices_to_update.append(neighbors)

        minimum_passes += 1

    updateMatrix(matrix, indices_to_update)
    return minimum_passes
'''


'''
Algo Time: O() | # Space: O():
Main Function
To check if the give matrix has a negative number, I will need to loop over the entire matrix.
I need to check if the current number is less than 0
I need to check if the up, down, left or right number is greater than 0
I need to store the current numbers index in an aux DS
I need to make updates to the matrix given the aux DS
    - Input: matrix
        - create negative_count DS
        - while negative_count > 0
            - loop over the entire matrix
            - if num >= 0
                - continue
            - increment negative count
            - look up, d, l, r
                - if neighbor > 0
                    - store idx in aux DS

            - if neg_count > 0
                - if length of aux DS == 0
                    - return -1

            - run update_matrix()
    - Output: integer
            - minimum_number
            - return -1, if all the negative integers can not be converted
'''

# Time: O(n^2) | # Space: O(n^2)


def minimum_passes_of_matrix_nn(matrix):
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])
    indices_to_update = []
    negative_count = 0
    minimum_passes = -1

    START = True
    while negative_count > 0 or START is True:
        negative_count = 0
        indices_to_update = []
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                idx = (row, col)
                num = matrix[row][col]
                if num >= 0:
                    continue
                negative_count += 1
                if found_postive_neighbors(idx, matrix) is True:
                    indices_to_update.append(idx)

        if negative_count > 0:
            if len(indices_to_update) == 0:
                return -1
        update_matrix(matrix, indices_to_update)
        minimum_passes += 1
        START = False

    return minimum_passes


'''
found_postive_neighbors
I need to check if a given indice's neighbors are > 0
    - Input: idx, matrix
        - for every idx in aux DS
            - update the matrix at that idx
                - multiply by -1
        -
    - Output: boolean
        - True, if a postive neighbor was found
        - False, if a postive neighbor was NOT found
'''


def found_postive_neighbors(idx, matrix):
    row = idx[0]
    col = idx[1]
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])

    # up
    if row > 0:
        if matrix[row - 1][col] > 0:
            return True
    # down
    if row < num_of_rows - 1:
        if matrix[row + 1][col] > 0:
            return True
    # left
    if col > 0:
        if matrix[row][col - 1] > 0:
            return True
    # right
    if col < num_of_cols - 1:
        if matrix[row][col + 1] > 0:
            return True

    return False


'''
update_matrix
- I need to update a given matrix at specified indices
    - Input: matrix, aux_DS
				-
        - for every idx in aux DS
            - update the matrix at that idx
                - multiply by -1
        -
    - Output:
			-
'''


def update_matrix(matrix, indices_to_update):
    for idx in indices_to_update:
        row = idx[0]
        col = idx[1]
        matrix[row][col] *= -1


matrix = [[0, -1, -3, 2, 0],
          [1, -2, -5, -1, -3],
          [3, 0, 0, -4, -1]]
print("matrix:", matrix)
print("minimum_passes_of_matrix_nn:", minimum_passes_of_matrix_nn(matrix))
print("matrix:", matrix)
'''
matrix =[[0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1]]
print("matrix:", matrix)
print("minimumPassesOfMatrix:", minimumPassesOfMatrix(matrix))
print("matrix:", matrix)
print(" ")

matrix =[[1, 0, 0, -2, -3],
        [-4, -5, -6, -2, -1],
        [0, 0, 0, 0, -1],
        [1, 2, 3, 0, -2]]
print("matrix:", matrix)
print("minimum_passes_of_matrix_nn:", minimum_passes_of_matrix_nn(matrix))
print("matrix:", matrix)
matrix =[[1, 0, 0, -2, -3],
        [-4, -5, -6, -2, -1],
        [0, 0, 0, 0, -1],
        [1, 2, 3, 0, -2]]
print("matrix:", matrix)
print("minimumPassesOfMatrix:", minimumPassesOfMatrix(matrix))
print("matrix:", matrix)
print(" ")


matrix =[[-2, -3, -4, -1, -9],
        [-4, -3, -4, -1, -2],
        [-6, -7, -2, -1, -1],
        [0, 0, 0, 0, -3],
        [1, -2, -3, -6, -1]]
print("matrix:", matrix)
print("minimum_passes_of_matrix_nn:", minimum_passes_of_matrix_nn(matrix))
print("matrix:", matrix)
matrix =[[-2, -3, -4, -1, -9],
        [-4, -3, -4, -1, -2],
        [-6, -7, -2, -1, -1],
        [0, 0, 0, 0, -3],
        [1, -2, -3, -6, -1]]
print("matrix:", matrix)
print("minimumPassesOfMatrix:", minimumPassesOfMatrix(matrix))
print("matrix:", matrix)
print(" ")

# _recursion
# _iteration
print(" ")
'''
