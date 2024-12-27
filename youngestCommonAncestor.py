'''youngestCommonAncestor.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")

'''
Type of Question:
- Graph Traversal

Clarifying Questions / Insights:
- The only way to traverse the problem is from the bottom to the top.
- manipulate the two descendant nodes so that they are on the same level

Base case:
-

Edge cases:
-

Question:
-

Input:
- Intuitive
    - topAncestor
    - descendantOne
    - descendantTwo
- Non-intuitive
    - all 1 to 3 inputs will be none.
    - Single Node
    - Two Node

Simplest Case:
- Three Node tree

Output:
- the youngest common ancestor of the two descendant nodes
'''

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

'''
Algo Time: O(n^2) | # Space: O(n):
- Starting from each descendant node.
- Traverse through the graph, at each node, store the node in an array.
- Starting from the descendant nodes, iterate through both arrays in a nested loop.
    - If the nodes are equal, then return the youngestCommonAncestor
'''

# Time: O(n^2) | # Space: O(n)
def getYoungestCommonAncestor_nn(topAncestor, descendantOne, descendantTwo):
    descendantOne_ancestor_array = [descendantOne]
    descendantTwo_ancestor_array = [descendantTwo]

    while descendantOne.ancestor is not None:
        descendantOne_ancestor_array.append(descendantOne.ancestor)
        descendantOne = descendantOne.ancestor

    while descendantTwo.ancestor is not None:
        descendantTwo_ancestor_array.append(descendantTwo.ancestor)
        descendantTwo = descendantTwo.ancestor

    for ancestorOne in descendantOne_ancestor_array:
        for ancestorTwo in descendantTwo_ancestor_array:
            if ancestorOne == ancestorTwo:
                return ancestorOne

    return None


'''
Algo Time: O(n) | # Space: O(1):
- Compute each of the descendant nodes depth
    - Input: descendant and topAncestor
        - create a variable to store the depth of the descendant and initalize it at zero
        - while the descendant is not equal to the ancestor, increment depth
    - Output: depth of the descendant node

- Find the lower descendant's ancestor that is on the equal depth as the higher descendant.
    - Input: lower_descendant, higher_descendant and the depth difference
        - For each differnece in depth, update the lower_descendant to the lower_descendant ancestor.
    - Output: lower_descendant's ancestor that has an equal depth as the higher descendant.

- Starting from each descendant at the same level, traverse until each descendant shares a common ancestor.
    - Input: lower_descendant, higher_descendant
        - While lower_descendant ancestor is not equal to higher_descendant ancestor: 
            update each descendant to their ancestor
    - Output: the descendant's common ancestor
'''

# Time: O(d) | # Space: O(1)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendantOne_depth = get_node_distance(topAncestor, descendantOne)
    descendantTwo_depth = get_node_distance(topAncestor, descendantTwo)
    depth_diff = abs(descendantOne_depth - descendantTwo_depth)

    if descendantOne_depth > descendantTwo_depth:
        descendantOne_ancestor = get_x_distance_ancestor(descendantOne, depth_diff)
        return get_youngest_common_ancestor(descendantOne_ancestor, descendantTwo)

    elif descendantTwo_depth > descendantOne_depth:
        descendantTwo_ancestor = get_x_distance_ancestor(descendantTwo, depth_diff)
        return get_youngest_common_ancestor(descendantOne, descendantTwo_ancestor)

    else:
        return get_youngest_common_ancestor(descendantOne, descendantTwo)

def get_node_distance(ancestor, descendant):
    distance = 0
    while descendant != ancestor:
        distance += 1
        descendant = descendant.ancestor
    return distance

def get_x_distance_ancestor(lower_descendant, depth_difference):
    lower_descendant_ancestor = lower_descendant
    while depth_difference > 0:
        lower_descendant_ancestor = lower_descendant_ancestor.ancestor
        depth_difference -= 1
    return lower_descendant_ancestor

def get_youngest_common_ancestor(descendantOne, descendantTwo):
    while descendantOne != descendantTwo:
        if descendantOne.ancestor is not None:
            descendantOne = descendantOne.ancestor
        if descendantTwo.ancestor is not None:
            descendantTwo = descendantTwo.ancestor
    return descendantOne