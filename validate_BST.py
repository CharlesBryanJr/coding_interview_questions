'''file_name'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
# BSTs
	# each node has a minimum and maximum value
	# if the node is on the LEFT side of root node
		# if the node is on the LEFT side of parent node:
			# minimum value: -inf
			# maximum value: parent node value - 1

		# if the node is on the RIGHT side of parent node:
			# minimum value: parent node value
			# maximum value: root node value

	# if the node is on the RIGHT side of root node:
		# if the node is on the LEFT side of parent node:
			# minimum value: root node value
			# maximum value: parent node value - 1

		# if the node is on the RIGHT side of parent node:
			# minimum value: parent node value
			# maximum value: inf

'''


# Time: O(n) | # Space: O(depth)
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validate_bst_recursion(tree, float("-inf"), float("inf"))


def validate_bst_recursion(current_node, min_value, max_value):

    # if we reached a leaf node
    if current_node is None:
        return True

    if current_node.value < min_value or current_node.value > max_value:
        return False

    parent_node = current_node
    valid_left_node = validate_bst_recursion(
        current_node.left, min_value, parent_node.value - 1)
    valid_right_node = validate_bst_recursion(
        current_node.right, parent_node.value, max_value)

    return valid_left_node and valid_right_node


def validateBst_iteration(tree):
    if tree is None:
        return True

    min_value = float("-inf")
    max_value = float("inf")

    tree_stack = [[tree, min_value, max_value]]

    while len(tree_stack) > 0:
        current_node, min_value, max_value = tree_stack.pop()

        if current_node.value < min_value or current_node.value > max_value:
            return False

        parent_node = current_node
        if current_node.left is not None:
            tree_stack.append(current_node.left, min_value,
                              parent_node.value - 1)

        if current_node.right is not None:
            tree_stack.append(current_node.right, parent_node.value, max_value)

    return True


# _iteration
print(" ")
