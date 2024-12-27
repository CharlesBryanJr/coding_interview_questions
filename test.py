'''LinkedListConstruction.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        self.head.prev = node
        self.head = node

    def setTail(self, node):
        self.head.prev = node
        self.head = node

    def insertBefore(self, node, nodeToInsert):
        if node == self.head and node == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.setHead(nodeToInsert)
        else:
            node.prev.next = nodeToInsert
            node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if node == self.head and node == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.setTail(nodeToInsert)
        else:
            node.next = nodeToInsert
            node.next.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        current_position = 1

        node = self.head
        while node is not None and current_position != position:
            node = node.next

        if node is None:
            self.setTail(nodeToInsert)
            return

        self.insertBefore(node, nodeToInsert)


    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                node_to_remove.remove(node_to_remove)

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.head = node.prev
        self.remove_pointers(node)

    def remove_pointers(self, node):
        if node.prev is not None:
            node.next.prev = node.prev
        if node.next is not None:
            node.prev.next = node.next
        node.prev = None
        node.next = None

    # Time: O(n) | # Space: O(1)
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        if node is None:
            return
        return node
