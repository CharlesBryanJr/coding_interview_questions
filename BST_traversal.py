'''BST_traversal.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

# In Order Traversal
# 1. Go Left
# 2. Visit
# 3. Go Right
# 4. Go Back
# Time: O(N) | # Space: O(N) / Space: O(d)


def inOrderTraverse_recursion(tree, array):
    if tree is not None:
        inOrderTraverse_recursion(tree.left, array)
        array.append(tree.value)
        inOrderTraverse_recursion(tree.right, array)

    return array


def inOrderTraverse_iteration(tree, array):
    # Set current to root of binary tree
    current = tree
    stack = []  # initialize stack

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif stack:
            current = stack.pop()
            array.append(current.value)

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break

    return array


# Pre Order Traversal
# 1. Visit
# 2. Go Left
# 3. Go Right
# 4. Go Back
# Time: O(N) | # Space: O(N) / Space: O(d)
def preOrderTraverse_recursion(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse_recursion(tree.left, array)
        preOrderTraverse_recursion(tree.right, array)

    return array


def preOrderTraverse_iteration(tree, array):
    if tree is None:
        return

    # create an empty stack and push root to it
    tree_stack = []
    tree_stack.append(tree)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left is processed first */
    while len(tree_stack) > 0:

        current_node = tree_stack.pop()

        array.append(current_node.value)

        if current_node.right is not None:
            tree_stack.append(current_node.right)

        if current_node.left is not None:
            tree_stack.append(current_node.left)

    return array

# Post Order Traversal
# 1. Go Left
# 2. Go Right
# 3. Visit
# 4. Go Back
# Time: O(N) | # Space: O(N) / Space: O(d)


def postOrderTraverse_recursion(tree, array):
    if tree is not None:
        postOrderTraverse_recursion(tree.left, array)
        postOrderTraverse_recursion(tree.right, array)
        array.append(tree.value)

    return array


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None
# A iterative function to do postorder traversal of
# a given binary tree


def postOrderTraverse_iteration(tree, array):
    if tree is None:
        return

    tree_stack = []

    while True:

        while tree:
            # Push root's right child and then root to stack
            if tree.right is not None:
                tree_stack.append(tree.right)

            tree_stack.append(tree)

            # Set root as root's left child
            tree = tree.left

        # Pop an item from stack and set it as root
        tree = tree_stack.pop()

        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and
                peek(tree_stack) == root.right):
            tree_stack.pop()  # Remove right child from stack
            tree_stack.append(root)  # Push root back to stack
            root = root.right  # change root so that the
            # right childis processed next

        # Else print root's data and set root as None
        else:
            array.append(tree.value)
            tree = None

        if len(tree_stack) <= 0:
            break

    return array


print(" ")
