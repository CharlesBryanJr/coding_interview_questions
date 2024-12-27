'''height_balanced_binary_tree.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- binary tree
- root node

actions:
- deteremine if each node is balanced, if so, the binary tree is balanced

return:
- Boolean True, if the given binary tree is balanced
- Boolean False, if the given binary tree is NOT balanced

note:
- balanced binary tree == the height of it's left subtree and right subtree differs by 1.
- for each node in the tree


'''

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, is_balanaced, height):
        self.is_balanaced = is_balanaced
        self.height = height

def height_balanced_binary_tree(node):
    if node is None:
        return TreeInfo(True, -1)
    left_subtree_info = height_balanced_binary_tree(node.left)
    right_subtree_info = height_balanced_binary_tree(node.right)

    is_subtrees_balanced = left_subtree_info.is_balanaced and right_subtree_info.is_balanaced
    subtree_height_difference = left_subtree_info.height - right_subtree_info.height

    is_node_balanced = is_subtrees_balanced and abs(subtree_height_difference) <= 1
    node_height = max(left_subtree_info.height, right_subtree_info.height) + 1

    return TreeInfo(is_node_balanced, node_height)

# Time: O(n) | # Space: O(h)
def heightBalancedBinaryTree(tree):
    if tree is None:
        return None

    tree_info = height_balanced_binary_tree(tree)
    return tree_info.is_balanaced

# _recursion
# _iteration
print(" ")