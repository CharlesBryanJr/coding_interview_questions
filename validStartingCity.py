'''validStaringCity'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(" ")

'''

Question:
- set of cities that form a circle
- connected by a circular road
- clockwise
- each city
    - has a gas station
    - some distance away from another city
- last city is connected to the first city
    - the distance in the distances array is the distance from the last city to the first
- drive to all citys without running out of gas
    - choose a starting city that makes this possible
- atleast one valid starting city
- distance[i] == distance from current city to the next
- fuel[i] == the amount of fuel at the current city's gas station
- sum(fuel) * mpg == sum(distances)
- tank starts on empty
- car's MPG:
    - postive integer
- at least two cities


Type of Question:
- Array
		- draw indices
		- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values

- Binary Trees
- Binary Search Trees
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

- Dynamic Programming
- Graphs
	- traverse through the graph DFS or BFS
			- for NON connected graphs, loop over every node
			- create and use a visited DS to optimize
	- trie edge == leads to a new descendant node
		- create a visited DS and initalize with false
	- back edge == leads to an already discovered ancestor node
		- if a back edge is exists == cycle
		- if a node is on the recursion stack and we reach it again
		- if a node is on the recursion stack, it is the ancestor of the current node
		- create a in_stack DS and initalize with false
	- cross edge == leads from one descendant to another already discovered descendant in a different subtree
	- forward edge == leads to an already discovered descendant node
- Greedy
	- 
- Heaps
- Linked List
- Recursion
- Searching
- Sorting
- Stacks
- Strings
- Tries

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Strings
			- Empty string
			- NULL or nil (and Optionals, depending on language)
			- Spaces (multiple words or sentences, or single/multiple whitespaces alone)
			- Punctuation
			- Upper, lowercase, or mixed (e.g., “stRiNg”)
			- Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
			- Different Languages (Diacritics? Unicode compliant? ASCII?)
			- Emoji 👍 (especially if question is presented as a text field input by a user)
			- Long String
		- Tuples
			- Named elements
		- Arrays
			- Empty array
			- Nested or not nested
		- Dictionaries (Hashmaps)
			- Collisions
		- Linked Lists (Stacks, Queues, Deques)
			- Circular
			- Loops (present or not?)
			- Doubly-Linked List

Observations / Clarifying Questions / Insights:
- only one valid starting city
- sum of (mpg * fuel[i]) == sum of distances[i] 

- simplest / smallest problem
	-

- If I knew / had this....
	- 
	- reverse this statement

Output (integer): the index of the valid starting city
- 
'''

''' 
Brute Force
Algo Time: O(n^2) | # Space: O(1):
Main Function

For each city in circle, I want to check if that city is a valid starting city
    If so, return the city
    If not, increment to the next city

    starting at a specfic, I need to check if the car can make it to the next city
        If so, continue
        If not, return false


    - Input (int, int, int): distances, fuel, mpg
		- valid_starting_city = False
        - tank = 0

        - loop over each city
            - city_count = 0
            - starting loop over each city
                - made_it_to_next_city = drive_to_next_city(ii, distances, fuel, mpg)
                - if made_it_to_next_city is False:
                    - break
                - increment city_count
            
            if city_count >= len(distances):
                valid_starting_city is True
    
            if valid_starting_city is True:
                return index
        
        - return -1
    - Output:
		-
'''

# Time: O(n^2) | # Space: O(1)


def validStartingCity_n_n(distances, fuel, mpg):
    num_of_cities = len(distances)

    for i in range(num_of_cities):
        tank = 0
        city_count = 0
        for ii in range(num_of_cities):
            city = i + ii
            if city > num_of_cities - 1:
                city = (i + ii) - num_of_cities

            tank += fuel[city] * mpg
            tank -= distances[city]

            if tank < 0:
                break

            city_count += 1

        if city_count == num_of_cities:
            return i

    return -1

# Time: O(n) | # Space: O(1)


def validStartingCity(distances, fuel, mpg):
    num_of_cities = len(distances)
    miles_remaining = 0
    starting_city = 0
    miles_remaining_at_starting_city = 0

    for city in range(1, num_of_cities):
        distance_from_last_city = distances[city - 1]
        fuel_from_preious_city = fuel[city - 1]

        miles_remaining += fuel_from_preious_city * mpg - distance_from_last_city

        if miles_remaining < miles_remaining_at_starting_city:
            miles_remaining_at_starting_city = miles_remaining
            starting_city = city

    return starting_city


distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
print("distances:", distances)
print("fuel:", fuel)
print("mpg:", mpg)
print("validStartingCity_n_n:", validStartingCity_n_n(distances, fuel, mpg))
print("validStartingCity:", validStartingCity(distances, fuel, mpg))
print(" ")
'''
distances = [10, 20, 10, 15, 5, 15, 25]
fuel = [0, 2, 1, 0, 0, 1, 1]
mpg = 20
print("distances:", distances)
print("fuel:", fuel)
print("mpg:", mpg)
print("validStartingCity:", validStartingCity(distances, fuel, mpg))
print(" ")

distances = [30, 40, 10, 10, 17, 13, 50, 30, 10, 40]
fuel = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mpg = 25
print("distances:", distances)
print("fuel:", fuel)
print("mpg:", mpg)
print("validStartingCity:", validStartingCity(distances, fuel, mpg))
print(" ")

# _recursion
# _iteration
print(" ")
'''
