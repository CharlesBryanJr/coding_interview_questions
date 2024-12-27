'''sumOfLinkedLists.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
import math
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
- Recursion
- Searching
- Sorting
- Stacks
- Strings
- Tries

Input:
- Intuitive(ll, ll): linkedListOne, linkedListTwo
    - two linked list
        - potentially unequal lengths
        - represents a non negative integer
        - each node is a digit of the integer
    -
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
- each node has a value and next pointer to the next node in the list
- the tail node points to None / null
- node values are from 0 - 9

Cases:
-

- simplest / smallest problem
	-

- If I knew / had this....
	-
	- reverse this statement

Output(linkedListTwo): the head of a new LL
- represents the sum of the integers represented by the two input linked list
'''

'''
Algo Time: O(max(m,n)) | # Space: O(max(m,n)):
Main Function

We need a way to figure out where the head of our linked list
    - create a dummy node that will point to the head of our linked list

We need to be able to reference the last node created in our linked lisk
    - create a variable that will store the last node created

We need to carry the remainder of the sum of the two node values divided by to the next iteration.
    - create a variable that will store the remainder

To iterate through the linked list, we will need to use the two head nodes as iterator variables
    - set the head node stored into each linked list in a variable

Iterate through the linked list
    # if we have a carry, node1 or node 2, continue to iterate

    to sum the value of each node in the two linked list, store the value in a variable
        if the two linked list are different lengths, its possible one of the nodes is none
        set sum_values to zero and only update to node.value if the node is not none 

    sum the value of the node in linkedListOne and linkedListTwo
        AND, take the modulo 10 of the sum
        # for this current iteration, create a node with a value 0-9
            # if the sum is greater than 9,
                # create a node with a value of the remainder after the sum has been divided by 10
                # and carry the quotient to the next iteration
    - sum = value1 + value2 + carry
    - node_value = sum % 10
    - node = LinkedList(node_value)

    - current_node.next = node
    - current_node = node

    add the new node created to the linked list
        set the last node's next pointer to point to the new node
        - current_node.next = node

    update the current node in the linked list to the node just created
        - current_node = node

    iterate the iterator variables to continue to traverse the linked list
        - if node1 is not None:
            - node1 = node1.next

        - if node2 is not None:
            - node2 = node2.next

-
    - Input():
        -
        -
    - Output():
			-
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algo Time: O(max(m,n)) | # Space: O(max(m,n)):
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    head_pointer = LinkedList(0)
    current_node = head_pointer
    node1 = linkedListOne
    node2 = linkedListTwo
    carry = 0

    while node1 is not None or node2 is not None or carry != 0:
        value1 = 0
        value2 = 0

        if node1 is not None:
            value1 = node1.value

        if node2 is not None:
            value2 = node2.value

        total = value1 + value2 + carry

        node_value = total % 10
        node = LinkedList(node_value)
        current_node.next = node
        current_node = node

        carry = total // 10

        if node1 is not None:
            node1 = node1.next

        if node2 is not None:
            node2 = node2.next

    return head_pointer.next


# Time: O(m + n) | # Space: O(m + n)
def sumOfLinkedLists_m_n(linkedListOne, linkedListTwo):
    LL_array1 = LL_to_array(linkedListOne)
    LL1_sum = sum_LL_array(LL_array1)

    LL_array2 = LL_to_array(linkedListTwo)
    LL2_sum = sum_LL_array(LL_array2)

    sum_of_LL = LL1_sum + LL2_sum
    summed_LL_array = num_to_array(sum_of_LL)

    head = array_to_LL(summed_LL_array)
    return head

def LL_to_array(linked_list):
    node = linked_list
    LL_array = []
    while node is not None:
        LL_array.append(node.value)
        node = node.next
    return LL_array

def sum_LL_array(array):
    LL_sum = 0
    for place in reversed(range(len(array))):
        LL_sum += array[place] * place_value(place)
    return LL_sum

def place_value(place):
    for i in range(0, place + 1):
        if i == place:
            return pow(10, place)

def num_to_array(num):
    array = []
    while num > 0:
        for place in range(num):
            if num / place_value(place) >= 10:
                continue
            value = num / place_value(place)
            value = math.floor(value)
            array.append(value)
            num -= value * place_value(place)
            break
    return array

def array_to_LL(array):
    for idx in range(len(array)):
        node_value = array[idx]
        if idx == 0:
            node = LinkedList(node_value)
            node.next = None
            last_node = node
            continue
        node = LinkedList(node_value)
        node.next = last_node
        last_node = node
    return node


# _recursion
# _iteration
print(" ")