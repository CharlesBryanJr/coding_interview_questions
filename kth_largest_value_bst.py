'''kth_largest_value_bst.ioy'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

# This is an input class. Do not edit.


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time: O(n) | # Space: O(n)


def in_order_traverse(node, sorted_node_values):
    if node is None:
        return

    in_order_traverse(node.left, sorted_node_values)
    sorted_node_values.append(node.value)
    in_order_traverse(node.right, sorted_node_values)


def findKthLargestValueInBst_n(tree, k):
    if tree is None:
        return -1
    sorted_node_values = []
    in_order_traverse(tree, sorted_node_values)
    return sorted_node_values[len(sorted_node_values) - k]

# Time: O(h+k) | # Space: O(h)


class Tree_Info:
    def __init__(self, visisted_nodes_count, last_node_value) -> None:
        self.visisted_nodes_count = visisted_nodes_count
        self.last_node_value = last_node_value


def reverse_in_order_traverse(node, k, tree_info):
    if node is None or tree_info.visisted_nodes_count >= k:
        return

    reverse_in_order_traverse(node.right, k, tree_info)
    if tree_info.visisted_nodes_count < k:
        tree_info.visisted_nodes_count += 1
        tree_info.last_node_value = node.value
        reverse_in_order_traverse(node.left, k, tree_info)


def findKthLargestValueInBst_1(tree, k):
    if tree is None:
        return -1

    tree_info = Tree_Info(0, -1)
    reverse_in_order_traverse(tree, k, tree_info)
    return tree_info.last_node_value
