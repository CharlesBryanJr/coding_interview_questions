'''phoneNumberMnemonics.py'''
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
		- draw indices
		- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values
		- running sums
		- sliding windows
			- start_of_window
			- end_of_window

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
 
	- 
- Searching
- Sorting
- Stacks
- Strings
- Tries

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Strings
			- Empty string
			- NULL or nil (and Optionals, depending on language)
			- Spaces (multiple words or sentences, or single/multiple whitespaces alone)
			- Punctuation
			- Upper, lowercase, or mixed (e.g., “stRiNg”)
			- Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
			- Different Languages (Diacritics? Unicode compliant? ASCII?)
			- Emoji 👍 (especially if question is presented as a text field input by a user)
			- Long String
		- Tuples
			- Named elements
		- Arrays
			- Empty array
			- Nested or not nested
		- Dictionaries (Hashmaps)
			- Collisions
		- Linked Lists (Stacks, Queues, Deques)
			- Circular
			- Loops (present or not?)
			- Doubly-Linked List

Observations / Clarifying Questions / Insights:
-

Cases:
-

- simplest / smallest problem
	-

- If I knew / had this....
	-
	- reverse this statement

Output:
-
'''

'''
Algo Time: O() | # Space: O():
Main Function

    - Input():
				#
        #
        #
    - Output():
			#
'''

# Time: O() | # Space: O()
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    return []

phoneNumber = "1905"
print("phoneNumber:", phoneNumber)
print("phoneNumberMnemonics:", phoneNumberMnemonics(phoneNumber))
print(" ")

phoneNumber = "1111"__annotations__
print("phoneNumber:", phoneNumber)
print("phoneNumberMnemonics:", phoneNumberMnemonics(phoneNumber))
print(" ")

phoneNumber = "4163420000"
print("phoneNumber:", phoneNumber)
print("phoneNumberMnemonics:", phoneNumberMnemonics(phoneNumber))
print(" ")

# _recursion
# _iteration
print(" ")