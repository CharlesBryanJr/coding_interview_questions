'''riverSizes.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")
import math

'''
Question:
- 

Type of Question
- Graph Traversal

Assumptions:
- 

Edge cases:
-

Input:
- two-dimensional array
    - matrix
    - potentially unequal height and width 
    - containing only 0's and 1's
    - 0 == land
    - 1 == river
- 
  
note:
- river == vertically and/or horizontally adjacent
    - not digonally adjacent
- river size == number of vertically and/or horizontally adjacent 1's
- a river can twist 


Algo:
-

Output:
- an array of all river sizes in the given two-dimensional array
    - order independent 

'''

# Time: O(rc) | # Space: O(rc)
def riverSizes(matrix):
    river_sizes = []
    visited = [[False for node in row] for row in matrix]

    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])

    for row in range(num_of_rows):
        for col in range(num_of_cols):
            
            if visited[row][col]:
                continue
            
            traverse_iteration(row, col, matrix, visited, river_sizes)

    return river_sizes
 
# depth first search
def traverse_iteration(row, col, matrix, visited, river_sizes):
    river_size = 0
    nodes_to_check = [[row, col]]
    
    while len(nodes_to_check) > 0:
        node_row_col = nodes_to_check.pop()
        row = node_row_col[0]
        col = node_row_col[1]
        
        if visited[row][col]:
            continue
        
        visited[row][col] = True
        
        if matrix[row][col] == 0:
            continue
        
        river_size += 1
        
        neighboring_unvisited_nodes = get_nodes_neighboring_unvisited_nodes(row, col, matrix, visited)
        for neighbor in neighboring_unvisited_nodes:
            nodes_to_check.append(neighbor)
        
    if river_size > 0:
        river_sizes.append(river_size)

def get_nodes_neighboring_unvisited_nodes(row, col, matrix, visited):
    neighboring_unvisited_nodes = []
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])
    
    # Top Node
    if row > 0 and not visited[row - 1][col]:
        neighboring_unvisited_nodes.append([row - 1, col])
    
    # Left Node
    if col > 0 and not visited[row][col - 1]:
        neighboring_unvisited_nodes.append([row, col - 1])

    # Right Node
    if col < num_of_cols - 1 and not visited[row][col + 1]:
         neighboring_unvisited_nodes.append([row, col + 1])
    
    # Bottom Node
    if row < num_of_rows - 1 and not visited[row + 1][col]:
        neighboring_unvisited_nodes.append([row + 1, col])
    
    return neighboring_unvisited_nodes


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
print("matrix:", matrix)
print("riverSizes:", riverSizes(matrix))
print(" ")


matrix = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]
print("matrix:", matrix)
print("riverSizes:", riverSizes(matrix))
print(" ")


matrix = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]
print("matrix:", matrix)
print("riverSizes:", riverSizes(matrix))
print(" ")

# _recursion
print(" ")
