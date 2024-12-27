'''sortStack'''
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
- Array
	- draw indices
	- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values

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
	- cross edge == leads from one descendant to another already discovered descendant in a different subtree
	- forward edge == leads to an already discovered descendant node
	- connected
        - zero island nodes
	- unweighted
        - the distance between all of the nodes is the exact same
	- undirected
        - travel in either direction
		- if a vertex appears in the edge list of another vertex (inverse will also be true)
		- if a vertex A is connected to vertex B, then vertex B is connected to Vertex A
- Greedy
	- 
- Heaps
- Linked List
	- keep track of node via temp variable
	- create a dummy node
- Recursion

Input:
- Intuitive
    - array of integers
        - representing a stack

Observations / Clarifying Questions / Insights:
- do not create a brand new array
- the array must be treated as a stack
- array[-1] == top of the stack
- remove elements
    - pop elements from the top of the stack
    - remove elements from end of the array
- add elements
    - append elements to the top of the stack
    - append elements to the end of the array
- visit elements
    - peak at elements at the top of the stack
    - access elements at the end of the array

Output: array
- a recursively sorted array
'''


'''
sort()
    - Input(stack):
		if the stack length is zero
            - if so, return the stack
        pop and store the top element in a variable
            - top = stack.pop()
        - sort the remainder of the stack
        - insert the element stored in top into the stack
    - Output():
			-
'''

'''
insert()
For a sorted stack
    locate the correct idx an element in the stack

    if the stack is empty OR if the element > element on the top
        add the element to the stack
        return none
    - Input():
		-
        -
        -
    - Output():
			-
'''

# Time: O(n^2) | # Space: O(n)


def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)
    insert(stack, top)
    return stack


def insert(stack, value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insert(stack, value)
    stack.append(top)


stack = [-5, 2, -2, 4, 3, 1]
print("stack:", stack)
print("sortStack:", sortStack(stack))
print(" ")

stack = [3, 3, 3, 3, 3, 3]
print("stack:", stack)
print("sortStack:", sortStack(stack))
print(" ")

stack = [2, 22, 222, 3, 33, 33, 9, 2, 3, 312, -9, -2, 3]
print("stack:", stack)
print("sortStack:", sortStack(stack))
print(" ")

# _recursion
# _iteration
print(" ")
