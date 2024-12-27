'''invert_binary_tree.py'''
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
- invert the given binary tree

return:
-

note:
- swap every left node with it's corresponding right node

'''
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def swap_child_nodes(node):
    node.left, node.right = node.right, node.left

# Time: O(n) | # Space: O(n)
def invertBinaryTree_iteration(tree):
    if tree is None:
        return None

    node_queue = [tree]

    while len(node_queue) > 0:
        node = node_queue.pop(0)
        if node is not None:
            swap_child_nodes(node)
            node_queue.append(node.left)
            node_queue.append(node.right)


# Time: O(n) | # Space: O(n)
def invertBinaryTree_recursion(tree):
    if tree is None:
        return None

    swap_child_nodes(tree)
    invertBinaryTree_recursion(tree.left)
    invertBinaryTree_recursion(tree.right)

print(" ")