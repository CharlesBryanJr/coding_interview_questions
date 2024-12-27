'''depth_first_search.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# Search Algortim
# Last In First Out

# Time: O(V+E) | # Space: O(V)


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)

        for child in self.children:
            child.depthFirstSearch(array)

        return array


print(" ")
