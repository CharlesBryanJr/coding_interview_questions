'''mergingLinkedLists.py'''
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
- the two linked list potentially merge at a shared intersection node

Type of Question:
- Linked List
	- keep track of node via temp variable
	- create a dummy node

Input:
- Intuitive
    - two linked list
        - potentially unequal length
        - each node has a value and next pointer
        -
    -

Observations / Clarifying Questions / Insights:
- do not modify either linked list
- do not create a new linked list
- all nodes following the intersection node are shared
    - return a linked list of all the shared nodes
        - head node == intersection node
-

Output: if the two linked list merge, return the intesection node
    - intesection node
    - None
'''

# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time: O(max(m,n)) | # Space: O(1)


def merging_linked_lists(linkedListOne, linkedListTwo):
    node1 = linkedListOne
    LL1_length = 0
    LL1_depth = 0
    node2 = linkedListTwo
    LL2_length = 0
    LL2_depth = 0

    while node1 is not None or node2 is not None:
        if node1 is not None:
            LL1_length += 1
            node1 = node1.next
        if node2 is not None:
            LL2_length += 1
            node2 = node2.next

    if LL1_length > LL2_length:
        equal_depth = LL1_length - LL2_length
        node1 = linkedListOne
        node2 = linkedListTwo
        for node in range(equal_depth):
            node1 = node1.next
            LL1_depth += 1

    elif LL2_length > LL1_length:
        equal_depth = LL2_length - LL1_length
        node1 = linkedListOne
        node2 = linkedListTwo
        for node in range(equal_depth):
            node2 = node2.next

# Time: O(max(m,n)) | # Space: O(1)


def mergingLinkedLists(linkedListOne, linkedListTwo):
    node1 = linkedListOne
    node2 = linkedListTwo

    while node1 is not node2:
        if not node1:
            node1 = linkedListTwo
        else:
            node1 = node1.next

        if not node2:
            node2 = linkedListOne
        else:
            node2 = node2.next

    return node1


# _recursion
# _iteration
print(" ")
