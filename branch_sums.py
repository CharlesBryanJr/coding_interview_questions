'''branch_sums.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# Given a Binary tree, return a list of each branch's sum
# Search Algortim
# Depth First Search
# Last In First Out

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# For each node in a branch,
# 1. Add the current node's value to the current branch's sum
# 2. Determine if the current node has child nodes
    # 3. Iterate to the current node's child nodes that are not None
    # 4. Repeat, Go back to 1
# 5. If the current node does not have child nodes, then the current node is a leaf node
# 6. Append the current branch's sum to the branch sums array.

# O(n) time | O(n) space
def calculate_branch_sum(root, running_branch_sum, branch_sums):
    # store the current node in variable
    current_node = root

    # if current node is none, return none
    if current_node is None:
        print("Current node is None", current_node)
        return None

    # 1. Add the current node's value to the current branch's sum
    running_branch_sum += current_node.value

    # 2. Determine if the current node has child nodes
        # 3. Iterate to the current node's child nodes that are not None
        # 4. Repeat, Go back to 1

    # IF the current node has a left node
    # THEN, call the function on the current node's left node
    # AND pass the current branch sum
    # AND pass the branch sums array
    if current_node.left is not None:
        calculate_branch_sum(current_node.left, running_branch_sum, branch_sums)

    # IF the current node has a right node
    # THEN, call the function on the  current node's right node
    # AND pass the current branch sum
    # AND pass the branch sums array
    if current_node.right is not None:
        calculate_branch_sum(current_node.right,running_branch_sum, branch_sums)

    # 5. If the current node does not have child nodes, then the current node is a leaf node
    # 6. Append the current branch's sum to the branch sums array.

    # IF the current node does NOT have child nodes (Leaf Node)
    # THEN, append the current branch's sum to the branch sums array.
    if current_node.left is None and current_node.right is None:
        branch_sums.append(running_branch_sum)


def branch_sums_recursion(root):
    # create array that will store all the sum of each branch
    branch_sums = []

    # call the recursive function that will
    # 1. sum each branch's nodes
    # 2. append each branch's sum to the branch sums array
    calculate_branch_sum(root, 0, branch_sums)

    return branch_sums


# O(n) time | O(n) space
def branch_sums_iteration(root):
    # create array that will store all the sum of each branch
    branch_sums = []

    # create a stack to store the nodes to traverse and the running branch sum
    node_stack = [(root, 0)]

    # iterate through each item in the stack
    # 1. sum each branch's nodes
    # 2. append each branch's sum to the branch sums array

    while len(node_stack) > 0:

        # ASSIGN the last node in the stack to the current node variable
        # ASSIGN the last node in the stack running sum to the running_branch_sum variable
        # and REMOVE the node
        # Note: The pop() method returns removed value.
        current_node, running_branch_sum = node_stack.pop()

        # if current node is none, return none
        if current_node is None:
            print("Current node is None", current_node)
            return None

        # 5. If the current node does not have child nodes, then the current node is a leaf node
        # 6. Append the current branch's sum to the branch sums array.

        # IF the current node does NOT have child nodes (Leaf Node)
        # THEN, add the running branch sum to the current nodes value
        # AND, append to the branch sums array.
        if current_node.left is None and current_node.right is None:
            branch_sums.append(running_branch_sum + current_node.value)

        # 2. Determine if the current node has child nodes
            # 3. add the current node's child nodes that are not None to the stack
            # 4. Repeat, Go back to 1

        # IF the current node has a right node
        # THEN, add the current node's right node
        # AND the running branch sum + current node's value to the stack
        if current_node.right is not None:
            node_stack.append((current_node.right, running_branch_sum + current_node.value))

        # IF the current node has a left node
        # THEN, add the current node's left node
        # AND the running branch sum + current node's value to the stack
        if current_node.left is not None:
            node_stack.append((current_node.left, running_branch_sum + current_node.value))

    return branch_sums


print(" ")
