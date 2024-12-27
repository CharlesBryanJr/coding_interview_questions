'''twoColorable'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
print(" ")

'''

Question:
- Given a matrix / adjacency array that represents a graph
- Two Colorable Graph / bipartite
	- all nodes must be assigned one of two colors
	- all edge connected nodes must have different colors

Type of Question:
- Array
	- draw indices

- Graphs
	- traverse through the graph DFS or BFS
			- for NON connected graphs, loop over every node
			- create and use a visited DS to optimize

Input:
- Intuitive
	- matrix
		- list of edges
	- connected
        - zero island nodes
	- unweighted
        - the distance between all of the nodes is the exact same
	- undirected
        - travel in either direction
		- if a vertex appears in the edge list of another vertex (inverse will also be true)
		- if a vertex A is connected to vertex B, then vertex B is connected to Vertex A
	- graph


Observations / Clarifying Questions / Insights:
- Two Colorable Graph / bipartite
	- all nodes must be assigned one of two colors
	- all edge connected nodes must have different colors
- the number of vertices in the graph is equal to the length of the edges
	- vertex_count == len(edges)
- each index in the adjacency list contains the vertex i's siblings
	- order independent
- each individual edge
	- positive integer
	- denotes an index in the list that this vertex is connected to
- self-loops
	- an edge that has the same destination and origin
	- an edge that connects a vertex to itself
	- makes the graph not 2 colorable / bipartite
-

- If I knew / had this....
	- if I knew if this graph had any self-loops
		- if so, return False
    - If i knew which node had the most siblings
	- reverse this statement

Output: boolean
- True, if the given graph is two-colorable
- False, if the given graph is NOT two-colorable
'''

'''
Algo Time: O() | # Space: O():
Main Function

Input(array): edges
    We need to store the color of each node.
    Create the colors array that will be the same length as the number of nodes.
    Initalized each node with the value "None"
    - num_of_nodes = len(edges)
    - colors = []
    - for node in range(num_of_nodes):
        - colors.append(None)
    
    Knowing we need to start at a node. 
    We can chose node 0, and update node 0's color to "True"
    So the first node can be colored as "True"
    Also, to start at node 0, we need to create a stack.
    Using the stack, we can traverse through the nodes in the graph, one node at a time.
    To start at node 0, we can initalize the stack at 0.
    - colors[0] = True
    - stack = [0]

    We need to traverse the graph.
    To do so, we will use the stack that we created.
    Traversing to the next node while the stack contains nodes.
    Each iteratation of the loop will have a node to investigate.
    while len(stack) > 0:
        node = stack.pop()
    
        For each node, we need to investigate each one of the node's connections
            For each connection of the current node, there are two possible cases.
            - for sibling in edges[node]:


            First, we have never seen the node before
                Which means the colors array at the connection idx is None
                If so, we can color the connection node in the colors array.
                    color the connection node the oppoiste color of the current node
                    add the connection node to the stack, so we can investigate it and it's connection nodes.
            - if colors[sibling] is None:
                - colors[sibling] = not colors[node]
                - stack.append(sibling)

            Second, we have seen this node before
                Which means the colors array at the connection idx has a color
                If the connection node is the same color as the current node.
                    Then this is not a two colorable graph
            - elif colors[sibling] == colors[node]:
                -  return False
    
    If we get to the end of the while loop, then we know, that we have
        assigned a color to each of the nodes 
        and 
        none of the nodes have a connection node that is the same color
    - return True

Output(boolean):
	True, if the graph can be Two Colorable
    False, if the graph can NOT be Two Colorable
'''

'''
# Time: O(v+e) | # Space: O(v)
def twoColorable(edges):
    num_of_nodes = len(edges)

    colors = []
    for node in range(num_of_nodes):
        colors.append(None)

    colors[0] = True
    stack = [0]

    while len(stack) > 0:
        node = stack.pop()

        for sibling in edges[node]:

            if colors[sibling] is None:
                colors[sibling] = not colors[node]
                stack.append(sibling)

            elif colors[sibling] == colors[node]:
                return False

    return True
'''

# Time: O(v+e) | # Space: O(v)


def twoColorable(edges):
    num_of_nodes = len(edges)
    colors = []
    for node in range(num_of_nodes):
        colors.append(None)

    colors[0] = True
    stack = [0]

    while len(stack) > 0:
        node = stack.pop()

        for sibling in edges[node]:

            if colors[sibling] is None:
                colors[sibling] = not colors[node]
                stack.append(sibling)

            elif colors[sibling] == colors[node]:
                return False

    return True

# Time: O(n^2) | # Space: O(n)


def twoColorable_nn(edges):
    num_of_nodes = len(edges)
    if num_of_nodes < 2:
        return False
    two_colorable = []
    for idx in range(num_of_nodes):
        two_colorable.append(None)

    num_of_siblings = []
    for idx in range(len(edges)):
        node = edges[idx]
        sibling_count = len(node)
        num_of_siblings.append(sibling_count)

    most_siblings = max(num_of_siblings)
    for idx in range(len(edges)):
        node = edges[idx]
        sibling_count = len(node)
        if sibling_count == most_siblings:
            two_colorable[idx] = "color 1"
            break

    num_of_nodes = len(edges)
    for idx in range(num_of_nodes):
        if two_colorable[idx] is not None:
            continue

        added_color = add_color(idx, two_colorable, edges)
        if added_color is False:
            return False

    return True


def add_color(node_idx, two_colorable, edges):
    two_colors = ["color 1", "color 2"]
    available_colors = [True, True]

    node = edges[node_idx]
    num_of_edges = len(node)
    for edge in range(num_of_edges):

        for idx in range(len(two_colors)):
            color = two_colors[idx]
            if two_colorable[edge] == color:
                available_colors[idx] = False

    for idx in range(len(available_colors)):
        available = available_colors[idx]
        color = two_colors[idx]
        if available:
            two_colorable[node_idx] = color
            return True

    return False


edges = [[1, 4],
         [0, 2, 3],
         [1, 4],
         [1],
         [0, 2]]
print("edges:", edges)
print("twoColorable_nn:", twoColorable_nn(edges))
print("twoColorable:", twoColorable(edges))
print(" ")
'''
edges =[[1, 4],
        [0, 2, 3],
        [1, 4],
        [1],
        [0, 2]]
print("edges:", edges)
print("twoColorable:", twoColorable(edges))
print(" ")

edges =[[2],
        [2, 3],
        [0, 1],
        [1]]
print("edges:", edges)
print("twoColorable:", twoColorable(edges))
print(" ")

# _recursion
# _iteration
print(" ")
'''
