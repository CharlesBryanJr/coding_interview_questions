'''zigzagTraverse.py'''
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
-

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

# Dictionaries (Hashmaps)
 # Understand how to add addition values to a key in a dictionary
    # for each key, create the values as a 2D array
    # when addition values need to be added to a key, append the addition values
	# Understand how to avoid duplicates
    # only add a key & value to a dictionary
    # at the last occurence/opportunity to create the key & value
    # or
    # add to a key's values in a dictionary
    # at the last occurence/opportunity to add to the key's values

- Binary Trees
- Binary Search Trees
		# each node has a minimum and maximum value
    	# if the node is on the LEFT side of root node
    		# if the node is on the LEFT side of parent node:
    			# minimum value: -inf
    			# maximum value: parent node value - 1

    		# if the node is on the RIGHT side of parent node:
    			# minimum value: parent node value
    			# maximum value: root node value

    	# if the node is on the RIGHT side of root node:
    		# if the node is on the LEFT side of parent node:
    			# minimum value: root node value
    			# maximum value: parent node value - 1

    		# if the node is on the RIGHT side of parent node:
    			# minimum value: parent node value
    			# maximum value: inf

- Dynamic Programming
	- 
- Graphs
	- traverse through the graph DFS or BFS
			- for NON connected graphs, loop over every node
			- create and use a visited DS to optimize
			- stack / queue
	- trie edge == leads to a new descendant node
		- create a visited DS and initalize with false
	- back edge == leads to an already discovered ancestor node
		- if a back edge is exists == cycle
		- if a node is on the recursion stack and we reach it again
		- if a node is on the recursion stack, it is the ancestor of the current node
		- create a in_stack DS and initalize with false
	# cross edge == leads from one descendant to another already discovered descendant in a different subtree
	# forward edge == leads to an already discovered descendant node
	# connected
     # zero island nodes
	# unweighted
		# the distance between all of the nodes is the exact same
	# undirected
        # travel in either direction
		# if a vertex appears in the edge list of another vertex (inverse will also be true)
		# if a vertex A is connected to vertex B, then vertex B is connected to Vertex A
# Greedy
	# 
# Heaps
# Linked List
	# keep track of node via temp variable
	# create a dummy node
# Recursion
	# the solution depends on solutions to smaller instances of the same problem
		# define the smaller instance of the problem
			# translate the for/while loop into a base case
	# will iterate/traverse until the function can return a value (base case)
		# always include return statment
	# base case == the smallest instance of the problem that can be solved directly
	# to keep track of element, store the element in a variable that connected to the recursion call
	# running variables left to right
			# arguments
	# running variables right to left
			# return statment
	# Recursive functions often take a sub array of the original array
	# the outcome of a recursive function will affect code on lines after it
	# To optimize use memoization
		# store the answer to recursive calls in a hash table
	# 1. Base Case
	# 2. Action
	# 3. update variables
	# 4. Recursion
		if idx >= len(array):
	
 
# Searching
# Sorting
# Stacks
# Strings
# Tries

Input():
# Intuitive
# Primitive Types
		# Numbers
			# Zero (0)
			# NULL or nil
			# Negative Numbers
			# Floats or Doubles (clarifies if Ints only?)
			# Min/Max Int
		# Strings
			# Empty string
			# NULL or nil (and Optionals, depending on language)
			# Spaces (multiple words or sentences, or single/multiple whitespaces alone)
			# Punctuation
			# Upper, lowercase, or mixed (e.g., “stRiNg”)
			# Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
			# Different Languages (Diacritics? Unicode compliant? ASCII?)
			# Emoji 👍 (especially if question is presented as a text field input by a user)
			# Long String
		# Tuples
			# Named elements
		# Arrays
			# Empty array
			# Nested or not nested
		# Dictionaries (Hashmaps)
			# Collisions
		# Linked Lists (Stacks, Queues, Deques)
			# Circular
			# Loops (present or not?)
			# Doubly-Linked List

Observations / Clarifying Questions / Insights:
# because the complexity of the zig zag traverse,
    # occurs on the perimeter of the matrix,
    # we need to be able to identify,
    # when our pointer is on the perimeter

Techniques & Tricks
# peaks and valleys of integers
# draw indices
# sorting
# running sums
# multiple pointers
# isolating idx or node
# modifying the input
	# hashing the index values, for 1 to n values
# sliding windows
	# start_of_window and end_of_window
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output():

'''

'''
# Time: O(n) | # Space: O(n)
Main Function

Because the complexity of the zig zag traverse,
occurs on the perimeter of the matrix,
we need to be able to identify,
when our pointer is on the perimeter,
during the traverse

Also, it is important to understand,
that wee need to keep track of,
the direction,
up or down,
that we are currently traversing in.




Input(matrix): array

height = len(array) - 1
width = len(array[0]) - 1
# since we need to know when are at the perimeter,
# of the matrix, and since the size of the,
# matrix will not change.
# we can just create two varaible,
# to store that information

result = []
# as we traverse in a zigzag order,
# we need to append each value at each index,
# to an output array,
# as requested by the problem statement

row = 0
col = 0
going_down = True
going_up = False
# to keep track of,
# where our pointer current is,
# and
# where our pointer is heading to next,
# in the traverse,
# we can create three variables,
# row, col, going_down
#
# the starting point of our,
# zigzag traverse will be,
# the 1st element in the matrix,
# or the 0th, 0th postion,
# and due this,
# the first direction of the traverse,
# will always be down

while not isOutOfBounds(row, col, height, width):
# to traverse in any order,
# let alone zigzag order
# we need our pointer to move,
# because of this,
# we will be incrementing and decrementing,
# row and col,
# which will move our pointer
#
# because the input size,
# of our matrix,
# will change,
# upon different inputs,
# we need to continue to move our pointer,
    # incrementing and decrementing,
    # row and col
# until we reach out of bounds,
# of the size of the matrix
#
# on each iteration of this while loop,
# the isOutOfBounds function will be called,
# and the isOutOfBounds function will,
# return True,
    # if our pointer,
    # row and col,
    # is out of bounds
# or
# return False
    # if our pointer,
    # row and col,
    # is out of bounds
#
# since we have not,
# in front of the function call,
# the while loop we break,
# if the pointer, row and col,
# is out of bounds,
# and
# continue to loop,
# while pointer, row and col,
# is in the bounds of the matrix

    results.append(array[row][col])
    # at this point,
    # we know that our pointer,
    # is in the bounds,
    # of the matrix
    #
    # so, we need to append the value,
    # of our current index,
    # to the output array


    # now, we need to move our pointer,
    # to the next zigzag order idx

    # it's important to understand,
    # where the pointer needs to,
    # "turned around"
    # during a zig zag traverse
        # the pointer needs to
        # "turned around" if either,
        # the pointer is at the,
        # left edge or bottom edge
        # or
        # the pointer is at the,
        # right edge or top edge

    # to help us make the decison
    # on where to move the pointer to,
    # we can reference,
    # the direction variables,
    # going_down and going_up
    # that we created
    #

    if going_down:
        if col == 0 or row == height:

        # if we are going DOWN
        # and we need to "turn around"
            # pointer is at the
            # left edge or bottom edge
        # we need to update,
        # going_down to False,
        # and
        # going_up to True,
            # because we are turning around
        # and
        # we need to move our pointer,
            # increment row OR col
        # we increment col,
        # if row == col
            # move our pointer,
                # to the right
            # because,
            # we have finished our traverse,
            # and we need to push,
            # the idx out of bounds,
            # to exit the while loop
        # we increment row,
        # if col == 0 and row != height
            # move our pointer,
                # down
            # because, we to
            # traverse unvisited idxs,
            # and the next diagonal,
            # to traverse,
            # would be the diagonal,
            # below it

        # if we are going DOWN
        # and we do NOT need to
        # "turn around"
            # pointer is NOT at the,
            # left edge or bottom edge

        # then we should continue,
        # going
        # digonally down
        # we can continue,
        # going digonally down,
        # by incremeting row
            # down
        # and decreming col
            # left
        #

    if going_up:
        if row == 0 or col = width:

        # if we are going DOWN
            # and we need to "turn around"
                # pointer is at the
                # top edge or right edge
            # we need to update,
            # going_up to False
            # going_down to True,
                # because we are turning around
            # and
            # we need to move our pointer
                # increment row OR col
            # increment row if,
            # col == width
                # move our pointer,
                    # down
                # because, we to
                # traverse unvisited idxs,
                # and the next diagonal,
                # to traverse,
                # would be the diagonal,
                # below it


            # increment col if,
            # row == 0 and col != width
                # move our pointer,
                    # right
                # because, we to
                # traverse unvisited idxs,
                # and the next diagonal,
                # to traverse,
                # would be the diagonal,
                # to the right

        # if we are going UP
        # and we do NOT need to
        # "turn around"
            # pointer is NOT at the,
            # top edge or right edge

        # then we should continue,
        # going
        # digonally up
        #
        # we can continue,
        # going digonally up,
        # by decremeting row
            # up
        # and incremeting col
            # right

return result
at this point, we have finished,
our traverse of the 2D array,
and we have appendx each idxs value,
to our output array in zigzag order

Output(array): array
# this 1D array will store the,
# zig zag order of the values stored in,
# the input array


def isOutOfBounds(row, col, height, width)
# return True,
    # if our pointer,
    # row and col,
    # is out of bounds
# or
# return False
    # if our pointer,
    # row and col,
    # is out of bounds
#
# the row and col parameters,
# will simulate the the location,
# of the pointer

    if row < 0:
        return True
    if row > height
        return True
    if col < 0:
        return True
    if col > width
        return True






'''

# Time: O(n) | # Space: O(n)
def zigzagTraverse_iteration(array):
    last_row = len(array) - 1
    last_col = len(array[0]) - 1
    zigzag_traverse = []

    row = 0
    col = 0
    down = True

    while row <= last_row and col <= last_col:
        num = array[row][col]
        zigzag_traverse.append(num)

        if down:
            if row == last_row:
                down = False
                col += 1

            elif col == 0:
                down = False
                row += 1

            else:
                row += 1
                col -= 1

        else:
            if col == last_col:
                down = True
                row += 1

            elif row == 0:
                down = True
                col += 1

            else:
                row -= 1
                col += 1

    return zigzag_traverse

# Time: O(n) | # Space: O(n)
def zigzagTraverse_recursion(array):
    zigzag_traverse = []
    zigzag(0, 0, True, array, zigzag_traverse)
    return zigzag_traverse

def zigzag(row, col, down, array, zigzag_traverse):
    last_row = len(array) - 1
    last_col = len(array[0]) - 1
    if row > last_row and col > last_col:
        return

    num = array[row][col]
    zigzag_traverse.append(num)

    if down:
        if row == last_row:
            down = False
            col += 1

        elif col == 0:
            down = False
            row += 1

        else:
            row += 1
            col -= 1

    else:
        if col == last_col:
            down = True
            row += 1

        elif row == 0:
            down = True
            col += 1

        else:
            row -= 1
            col += 1

    zigzag(row, col, down, array, zigzag_traverse)

array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]]
print("array:", array)
print("zigzagTraverse_iteration:", zigzagTraverse_iteration(array))
print("zigzagTraverse_recursion:", zigzagTraverse_recursion(array))
print(" ")
'''
array =[[1, 3],
        [2, 4],
        [5, 7],
        [6, 8],
        [9, 10]]
print("array:", array)
print("zigzagTraverse:", zigzagTraverse(array))
print(" ")

array = [
    [1, 21, -3, 4, 15, 6, -7, 88, 9],
    [10, 11, 112, 12, 20, -1, -2, -3, -4],
    [6, 8, 113, 19, 21, 0, 0, 0, 0],
    [7, 2, 18, 22, -27, 12, 32, -111, 66],
    [15, 17, 23, 226, 28, -28, -226, -23, -17],
    [16, 24, 27, 299, 30, 29, 32, 31, 88]
]
print("array:", array)
print("zigzagTraverse:", zigzagTraverse(array))
print(" ")

# _recursion
# _iteration
print(" ")
'''