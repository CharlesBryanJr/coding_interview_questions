'''merge_binary_trees.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- two binary trees

action:
- merge the two given binary trees
- iterate through both trees in the same order
- create new or update an existing tree

return:
- merged binary trees

note:
- overlapping nodes: sum their values
- use depth first search



'''

# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time: O(n) | # Space: O(h)
def merge_binary_trees_recursion(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value += tree2.value

    tree1.left = merge_binary_trees_recursion(tree1.left, tree2.left)
    tree1.right = merge_binary_trees_recursion(tree1.right, tree2.right)

    return tree1

# Time: O(n) | # Space: O(h)
# depth first search
def merge_binary_trees_iteration(tree1, tree2):
    if tree1 is None:
        return tree2

    tree1_stack = [tree1]
    tree2_stack = [tree2]

    while len(tree1_stack) > 0:
        tree1_node = tree1_stack.pop()
        tree2_node = tree2_stack.pop()

        if tree2_node is None:
            continue

        tree1_node.value += tree2_node.value

        if tree1_node.left is None:
            tree1_node.left = tree2_node.left
        else:
            tree1_stack.append(tree1_node.left)
            tree2_stack.append(tree2_node.left)

        if tree1_node.right is None:
            tree1_node.right = tree2_node.right
        else:
            tree1_stack.append(tree1_node.right)
            tree2_stack.append(tree2_node.right)

    return tree1


# _recursion
# _iteration
print(" ")
