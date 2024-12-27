'''binary_tree_diameter.py'''
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

action:
- find all paths
- count the length of each path
- return the path with the largest length

return:
- the given binary's tree diameter

note:
- binary's tree diameter == length of the longest path
- path == a collection of connected nodes, where each node is only connected to two or less nodes
- path length == number of edges between the path's first and last node


For any given node, the node's diameter is
- the depth of the node's left subtree
- or
- the depth of the node's right subtree
- or
- the length of a path that can be created using the node


'''
# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diamter, height):
        self.diamter = diamter
        self.height = height


def get_TreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    left_TreeInfo = get_TreeInfo(tree.left)
    right_TreeInfo = get_TreeInfo(tree.right)

    longest_path_through_root = left_TreeInfo.height + right_TreeInfo.height
    current_max_diameter = max(left_TreeInfo.diamter, right_TreeInfo.diamter)
    current_diameter = max(longest_path_through_root, current_max_diameter)
    current_height = 1 + max(left_TreeInfo.height, right_TreeInfo.height)

    return TreeInfo(current_diameter, current_height)

# Time: O(n) | # Space: O(h)
def binaryTreeDiameter(tree):
    return get_TreeInfo(tree).diamter


# _recursion
# _iteration
print(" ")
