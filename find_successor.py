'''find_successor.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- a binary tree
    - value
    - left
    - right
    - parent
- node value

action:
-
return:
- a given node's successor

note:
- a node's successor is the next node to be visited
    - furtherst left node in the node's right subtree
- use in order traversal
- the last node does not have a successor
- the root node's parent node is none
- each node has a parent node
- assuming the given node value is a node in the binary tree
'''


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def in_order_traversal(node, array):
    if node is None:
        return

    in_order_traversal(node.left, array)
    array.append(node)
    in_order_traversal(node.right, array)

    return array

# Time: O(n) | # Space: O(n)
def find_successor(tree, node):
    if tree is None:
        return

    array = []
    in_order_traversal(tree, array)

    for idx, num in enumerate(array):
        if idx == len(array) - 1:
            return None

        if num == node:
            return array[idx + 1]


def get_left_most_child(node):
    current_node = node

    while current_node.left is not None:
        current_node = current_node.left

    return current_node


def get_right_most_parent(node):
    current_node = node

    while current_node.parent is not None and current_node.parent.right == current_node:
        current_node = current_node.parent

    return current_node.parent


# Time: O(h) | # Space: O(1)
def findSuccessor(tree, node):

    if node.right is not None:
        return get_left_most_child(node.right)

    return get_right_most_parent(node)


# _recursion
# _iteration
print(" ")
