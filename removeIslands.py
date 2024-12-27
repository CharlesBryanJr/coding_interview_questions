'''removeIslands.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")

'''

Type of Question:
- matrix
- graph traversal

Clarifying Questions / Insights:
- an island is any one that is not connected to the border

Edge cases:
-

Base case:
-

Question:
-

Input:
- Intuitive
    - 2D Array
    - potenitally unequal height and width
    - contains only 0s and 1s
    - 1 == black
    - 0 == white
    - Island = 1's that are horizontally or vertically adjacent
    - Islands can not have 1's in the first row, first column, last row or last column
- Non-intuitive

- If I knew/ had this....
    - to know where the 1's are that are connected to the border.

Output:
- the given matrix without islands

'''

'''
Brute force approach:

Loop over each location in the matrix
If a location is storing the value 1,
    - treat the location as node
    - perform a graph traversal
    - to find all of the other 1's connected to current node.
    - If any of the connected ones are a border node, do nothing,
    - If none of the connected ones are boder nodes, replace all with 0 
'''

'''
Optimized approach:

Algo Time: O(n) | # Space: O(n):
Given islands can not be connected to the border, it would be helpful to know where the 1's are that are connected to the border.
- Create an auxiliary DS of same dimensions of given matrix
    - Store which postions are connected to the border
    - initalize auxiliary DS with False

Find and update auxiliary DS with locations of nodes connected to the border
- Loop over each border of the given matrix (top, left, right, bottom)
    - Find all of the 1's that are connected to the border
        - performed a DFS on all of the 1's on the border
            - DFS looked for verically and horizontally adjacent 1's
                - if already connected to the border
                    - skip
                - else: update the corresponding position in the auxiliary DS to True
        -

Replace all 1's that are not connected to the border with zero
- loop over the interior matrix
    - replace all 1's to 0 that have a corresponding value False in the auxiliary DS

    - Input:
        -
        -
    - Output:
'''

# Time: O(wh) | # Space: O(wh)


def removeIslands(matrix):
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])
    border_islands = [[False for col in matrix[0]] for row in matrix]

    for row in range(num_of_rows):
        for col in range(num_of_cols):

            if not border_node(row, col, matrix):
                continue

            if matrix[row][col] == 0:
                continue

            traverse_neighbors(row, col, matrix, border_islands)

    for row in range(1, num_of_rows - 1):
        for col in range(1, num_of_cols - 1):
            if border_islands[row][col] is True:
                continue

            matrix[row][col] = 0

    return matrix

# depth first search


def traverse_neighbors(start_row, start_col, matrix, border_islands):
    neighbors = [[start_row, start_col]]

    while len(neighbors) > 0:
        postion = neighbors.pop()
        row = postion[0]
        col = postion[1]

        visited = border_islands[row][col]
        if visited:
            continue

        border_islands[row][col] = True

        neighbors_to_add = get_neighbors(row, col, matrix)
        for neighbor in neighbors_to_add:
            row = neighbor[0]
            col = neighbor[1]

            if matrix[row][col] == 0:
                continue

            neighbors.append(neighbor)


def get_neighbors(row, col, matrix):
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])
    neighbors = []

    # top
    if row - 1 >= 0:
        neighbors.append([row - 1, col])

    # down
    if row + 1 < num_of_rows:
        neighbors.append([row + 1, col])

    # left
    if col - 1 >= 0:
        neighbors.append([row, col - 1])

    # right
    if col + 1 < num_of_cols:
        neighbors.append([row, col + 1])

    return neighbors


def border_node(row, col, matrix):
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])

    if row == 0:
        return True
    if col == 0:
        return True
    if num_of_rows - 1 == row:
        return True
    if num_of_cols - 1 == col:
        return True

    return False


matrix = [[1, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 1, 1],
          [0, 0, 1, 0, 1, 0],
          [1, 1, 0, 0, 1, 0],
          [1, 0, 1, 1, 0, 0],
          [1, 0, 0, 0, 0, 1]]
print("matrix:", matrix)
print("removeIslands:", removeIslands(matrix))
print(" ")

matrix = [[0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0]]
print("matrix:", matrix)
print("removeIslands:", removeIslands(matrix))
print(" ")

matrix = [[1, 1],
          [1, 1]]
print("matrix:", matrix)
print("removeIslands:", removeIslands(matrix))
print(" ")

# _recursion
# _iteration
print(" ")
