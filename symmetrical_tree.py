'''symmetrical_tree.py'''
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

action:
- for any given node,
    - IF, the value of left child == value of right child 
    - IF, the left child's left child == the right child's right child
    - IF, the left child's right child == the right child's left child
    - THEN, node is symmetrical

return:
- boolean True, if symmetrical
- boolean False, if NOT symmetrical

note:
- symmetrical binary tree == if left and right subtrees are mirror images of each other
- root node is irrelevant


'''
# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, value, height):
        self.value = value
        self.height = height
        self.is_symmetrical = None

# Time: O(n) | # Space: O(h)
def symmetrical_tree(left_tree, right_tree):

    if left_tree is not None and right_tree is not None:
        if left_tree.value == right_tree.value:
            return symmetrical_tree(left_tree.left, right_tree.right) and symmetrical_tree(left_tree.right, right_tree.left)

    return left_tree == right_tree


def symmetricalTree(tree):
    return symmetrical_tree(tree.left, tree.right)


# Time: O(n) | # Space: O(h)
def symmetrical_tree_iteration(tree):
    if tree is None:
        return

    left_stack = [tree.left]
    right_stack = [tree.right]

    while len(left_stack) > 0:
        left_node = left_stack.pop()
        right_node = right_stack.pop()

        if left_node is None and right_node is None:
            continue

        if left_node is None or right_node is None:
            return False

        if left_node.value != right_node.value:
            return False

        left_stack.append(left_node.left)
        right_stack.append(right_node.right)

        left_stack.append(left_node.right)
        right_stack.append(right_node.left)

    return True


# _recursion
# _iteration
print(" ")
