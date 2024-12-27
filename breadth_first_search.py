'''breadth_first_search.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- an empty arry
action:
- store names in the given empty array in order of breadth first search
return:
-
note:
- It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. 
- Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.
- Queue: FIFO
    - pop the first node in the queue
    - add the node's name to the array
    - add it's two child nodes to the end of the queue

'''


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time: O(v+e) | # Space: O(v)
    def breadthFirstSearch(self, array):
        node_queue = [self]

        while len(node_queue) > 0:
            node = node_queue.pop(0)
            array.append(node.name)
            for child in node.children:
                node_queue.append(child)

        return array


print(" ")
