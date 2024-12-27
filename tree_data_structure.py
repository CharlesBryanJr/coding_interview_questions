'''tree_data_structure.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# CONSTRAINTS
# 1. All keys must be the same type
# 2. What if keys are equal?


class Node:

    def __init__(self, key, value, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Tree:

    def __init__(self) -> None:
        self.root = None

    def contains(self, key):
        found = False
        current = self.root

        while current is not None and found is False:

            if current.key == key:
                found = True

            elif key < current.key:
                current = current.left

            else:  # key > current.key:
                current = current.right

        return found

    def update(self, key, value):

        if self.root is None:
            self.root = Node(key, value)
            return None

        current = self.root

        while current is not None:

            if current.key == key:
                current.value = value
                break

            if key < current.key:

                if current.left is None:
                    current.left = Node(key, value)
                    break

                current = current.left

            else:  # key > current.key:

                if current.right is None:
                    current.right = Node(key, value)
                    break

                current = current.right

        return None

    def get_value(self, key):
        value = None
        current = self.root

        while current is not None:

            if current.key == key:
                value = current.value
                break

            if key > current.key:
                current = current.right

            else:  # key < current.key:
                current = current.left

        return value

    def traverse(self, current, arr):

        if current is not None:
            arr.append(current.key)
            self.traverse(current.left, arr)
            self.traverse(current.right, arr)

    def keys(self):
        arr = []
        self.traverse(self.root, arr)
        return arr

    def values(self):
        keys = self.keys()
        return [self.get_value(key) for key in keys]


tree1 = Tree()
tree1.update("a", 13)
tree1.update("b", 47)
tree1.update("c", 5)
tree1.update("c", 33)
print("Keys:", tree1.keys())
print("Values:", tree1.values())
print("Get a:", tree1.get_value("a"))

print(" ")
