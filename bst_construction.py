'''bst_construction.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Avg: O(log(n) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        # create a new node in the BST with the given value

        # store the current node in a variable
        current_node = self

        # start while loop
        while True:

            if value < current_node.value:

                # if the given value less than the current node's value
                # if the current node does NOT have a left node,
                # THEN, add a new node using the given value
                # AND, exit the while loop
                if current_node.left is None:
                    current_node.left = BST(value)
                    break

                # if the given value less than the current node's value
                # if the current node does have a left node,
                # THEN, iterate to the current node's left node
                # UPDATE the current node to the current node's left node
                else:
                    current_node = current_node.left

            else:
                # if the given value greater than or equal to the current node's value
                # if the current node does NOT have a right node,
                # THEN, add a new node using the given value
                # AND, exit the while loop
                if current_node.right is None:
                    current_node.right = BST(value)
                    # after adding the new node, exit the while loop
                    break

                # if the given value greater than or equal to the current node's value
                # if the current node does have a right node,
                # THEN, iterate to the current node's right node
                # UPDATE the current node to the current node's right node
                else:
                    current_node = current_node.right

        return self

    # Avg: O(log(n) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        # Does the BST contain a node with the same value as the given value?

        # store the current node in a variable
        current_node = self

        while current_node is not None:
            # if the current node exists
            # if the given node value is less than the current node's value
            # THEN, iterate to the current node's left node
            # UPDATE the current node to the current node's left node
            if value < current_node.value:
                current_node = current_node.left

            # if the current node exists
            # if the given node value is greater than the current node's value
            # THEN, iterate to the current node's right node
            # UPDATE the current node to the current node's right node
            elif value > current_node.value:
                current_node = current_node.right

            # if the current node exists
            # if the given node value is equal than the current node's value
            # THEN, the BST does contain a node with the same value as the given value
            else:
                return True

        # the BST does NOT contain a node with the same value as the given value
        return False

    def get_tree_min_value(self):
        # store the current node in a variable
        current_node = self

        # to obtain the smallest value in a BST, find the left most node's value
        # assign the current node value to min_value
        # update the current node with the current node's left most value
        while current_node is not None:
            min_value = current_node.value
            current_node = current_node.left

        return min_value

    def get_tree_max_value(self):
        # store the current node in a variable
        current_node = self

        # to obtain the largest value in a BST, find the right most node's value
        # assign the current node value to max_value
        # update the current node with the current node's right most value
        while current_node is not None:
            max_value = current_node.value
            current_node = current_node.right

        return max_value

    # Avg: O(log(n) time | O(1) space
    # Worst: O(n) time | O(1) space
    def remove(self, value, parent_node=None):
        # if the BST contains a node with the same value as the given value,
        # then remove that node and update the affected subtree nodes.

        # store the current node in a variable
        current_node = self

        # if the current node exists
        while current_node is not None:

            # if the current node exists
            # if the node to remove value is less than the current node's value
            # THEN, iterate to the current node's left node
            # AND, update the parent node to the current node
            # AND, update the current node to the current node's left node
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            # if the current node exists
            # if the node to remove value is greater than the current node's value
            # THEN, iterate to the current node's right node
            # AND, update the parent node to the current node
            # AND, update the current node to the current node's right node
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            else:  # value > current_node.value:
                # if two child nodes
                # if one child node
                # if left child node exist
                # if right child node exist
                # if no child nodes
                # if no parent nodes (root node)

                # if the current node exists
                # if the node to remove value is equal to the current node's value
                # if the current node does NOT have a parent node (root node)
                # if the current node has both a left and right node
                # THEN, search the right subtree for the node with the smallest value
                # AND update the current node's value with the right subtree's smallest value
                # AND remove the node with the smallest value

                if current_node.left is not None and current_node.right is not None:
                    min_value = current_node.right.get_tree_min_value()
                    current_node.value = min_value
                    current_node.right.remove(min_value, current_node)

                elif parent_node is None:

                    # if the current node exists
                    # if the node to remove value is equal to the current node's value
                    # if the current node does NOT have a parent node (root node)
                    # if the current node has a left child node
                    # if the current node's left node exists
                    # if the current node is equal to the parent node's left node
                    # THEN, replace the parent node's left node with the current node left node
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left

                    # if the current node exists
                    # if the node to remove value is equal to the current node's value
                    # if the current node does NOT have a parent node (root node)
                    # if the current node has one child node
                    # if the current node's right node exists
                    # if the current node is equal to the parent node's right node
                    # THEN, replace the parent node's right node with the current node's right node
                    if current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right

                    # if the current node exists
                    # if the node to remove value is equal to the current node's value
                    # if the current node does NOT have a parent node (root node)
                    # if the current node does NOT have child nodes
                    # THEN, update the current node's value to 'None'
                    else:  # single node tree
                        current_node.value = None

                elif current_node == parent_node.left:
                    if current_node.left is not None:
                        parent_node.left = current_node.left

                    else: # current_node.right is not None:
                        parent_node.left = current_node.right

                elif current_node == parent_node.right:
                    if current_node.left is not None:
                        parent_node.right = current_node.left

                    else: # current_node.right is not None
                        parent_node.right = current_node.right

                break

        return self


tree1 = BST(10)
tree1.insert(5)
tree1.insert(8)
tree1.remove(5)
tree1.remove(15)
tree1.remove(10)


print(" ")
