'''remove_duplicates.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# given the head of a singly linked list
# sorted in order of node value

# remove nodes with duplicate values and return the modified linked list

# identify the duplicate value
# reassign the first occurrence of a value next pointer to the next node that has a different value



# Time: O(n) | # Space: O(1)

def remove_duplicates_recursion(linkedList):
    pass

def remove_duplicates_iteration(linkedList):

    if linkedList is None:
        return linkedList

    current_node = linkedList

    while current_node is not None:
        next_unqiue_node = current_node.next

        while next_unqiue_node is not None and next_unqiue_node.value == current_node.value:
            next_unqiue_node = next_unqiue_node.next
        
        current_node.next = next_unqiue_node
        current_node = next_unqiue_node

    return linkedList

print(" ")
