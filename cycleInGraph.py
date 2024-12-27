'''cycleInGraph'''
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
- graph

Input:
- Intuitive
    - list of edges == unweighted directed graph
    - at least one node

- Non-intuitive

Clarifying Questions / Insights:
- cycle == any number of vertices that are connected in a closed chain 
    - one vertex counts
    - in a chain of vertices, the first vertex is also the last vertex
- adjacency list == graph
    - may contain self loops
    - each postive integer ==
        - edge
        - destination vertex that connects to the current vertex
- number of edges == length of the edges
- directed graph
    - one way
- self loop == cycle
    - an edge that hase the same destination and orgin

- trie edge == leads to a new descendant node
- back edge == leads to an already discovered ancestor node
- cross edge == leads from one descendant to another already discovered descendant in a different subtree
- forward edge == leads to an already discovered descendant node


- the aggregate of every index's adjacency list in the cycle must contain each index
- whenever a descendant's edge leads to an ancestor node, we have a cycle

- If I knew / had this....
	- if I knew every time that a descendant's node had a back edge to an ancestor, I could find all of the cycles
    - if the graph had a back edge

Output:
- True, if the given graph contains a cycle
- False, if the given graph does not contain a cycle
'''

'''
Algo Time: O(v+e) | # Space: O(v):
Main Function
- Input: edges
    For potenially NON connected graphs, we need to know if we have visited a specfic node before
        - Create a visited data structure of the same length of the given matrix
        - Initalize with Zero / False

    To determine if a node has a back edge, we can use a recursion stack and lookup if a specfic node is in the stack
        - create a in_stack data structure of the same length of the given matrix
        - Initalize with Zero / False

    Perform a DFS on every node in the graph.
    For potenially non connected graphs, to ensure a DFS is peformed on every node in the graph
    We need to loop over every node in the graph and use a visited DS to optimize.
    - loop over every node in the length of the graph
        - continue to the next node if the node has already been visisted
        - call DFS on current node
            - return True, if DFS on current node returns true

    - False, if a cycle is not found while performing a DFS on every node in the graph
'''

'''
DFS Function
Determine if the current node is contained within a cycle
If the current node has an outbound edge to a node already in the stack, then we have found a cycle.
We need to loop over every outbound edge from the current node and check if the the outbound edge points to a node in the stack.
We need to update our auxiallary data structure

    - Input: edges, node index, visited, in_stack
        To keep our auxiallary DS updated, we need to update the current node's status to visited and in the stack
        - update the visited DS at the index of the input to True
        - update the in_stack DS at the index of the input to True

        To loop over every outbound edge from the current node, we should store those edges in a aux DS.
            - loop over every outbound edge from the node
                - if the outbound edge has not been visited
                    - call DFS function on current outbound edge
                        - return True, if DFS on current outbound edge returns true
                - if the outbound edge has been visited and the outbound edge is in the stack
                    - return True
        
        we need to remove the current node from the stack
            - we can set the node's location in the stack to false
        
        - False, if a cycle is not found while performing a DFS on every outbound edge from the current node

    - Output:
        - True, if the input node has an edge that has been visited and is on the stack
        - False, else
'''

# Time: O(v + e) | # Space: O(v)


def cycleInGraph(edges):
    graph_length = len(edges)
    visited = []
    in_stack = []

    for idx in range(graph_length):
        visited.append(False)
        in_stack.append(False)

    for node in range(graph_length):
        if visited[node] is True:
            continue

        found_cycle = is_node_in_cycle(node, edges, visited, in_stack)
        if found_cycle is True:
            return True

    return False


def is_node_in_cycle(node, edges, visited, in_stack):
    visited[node] = True
    in_stack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            found_cycle = is_node_in_cycle(neighbor, edges, visited, in_stack)
            if found_cycle is True:
                return True
        elif in_stack[neighbor] is True:
            return True

    in_stack[node] = False
    return False


edges = [[1, 3],
         [2, 3, 4],
         [0],
         [],
         [2, 5],
         []]
print("edges:", edges)
print("cycleInGraph:", cycleInGraph(edges))
print(" ")

edges = [[1, 2],
         [2],
         []]
print("edges:", edges)
print("cycleInGraph:", cycleInGraph(edges))
print(" ")

edges = [[1],
         [2, 3, 4, 5, 6, 7],
         [],
         [2, 7],
         [5],
         [],
         [4],
         [0]]
print("edges:", edges)
print("cycleInGraph:", cycleInGraph(edges))
print(" ")

# _recursion
# _iteration
print(" ")
