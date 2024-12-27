'''staircaseTraversal.py'''
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
- Recursion
	- the solution depends on solutions to smaller instances of the same problem
		# how many ways is there to reach step 1, and step 2
	- will iterate/traverse until the function can return a value (base case)
		- always include return statment
	- to keep track of element, store the element in a variable that connected to the recursion call
	- running variables can be passed as arguments
	- Recursive functions often take a sub array of the original array
	- code on lines after of a recursive call will be

Input:
- Intuitive
	- Given two positive integers
		- height of a staircase
			- step size/length
		- max number of steps that you can advance up the staircase at a time

Observations / Clarifying Questions / Insights:
- step size/length <= height
- the number of ways to get to the steps that are within the range of max steps from the final step
    - will sum up to the ways to get to the final step.
-

Output:
	- return the number of ways you can climb the staircase
'''

'''
Algo Time: O() | # Space: O():
Main Function

This implementation capitalizes on the already stored values in the data structure 
    and only does the necessary operations to calculate the next result

- Input(int, int): height, maxSteps

we need create a DS that will store the number of ways_to_top for any given height
    this DS range should be 0 to the height of the staircase
    for the heights that are the base cases, height <= 1
        we can initalize those values
        - ways_to_top[0] = 1
        - ways_to_top[1] = 1

we need create a variable that will store the current number of ways_to_top
    ths variable will be a running sum
    initalize at 0
    - current_ways_to_top = 0


    to find the number of ways_to_top for the current height
        sum the last (height - maxSteps) elements in the data structure

        For each height in the range of 1 to the final height
        - for current_height in range(1, height + 1):

            to simulate sliding the window, we need to calucate the start and end
            calculate the start of the window
                this will increment the lower bound by 1
            calculate the end of the window
                this will increment the upper bound by 1
            - start_of_window = current_height - maxSteps - 1
            - end_of_window = current_height - 1

            to simulate sliding the window, we need to decrement and then increment
            if possible, decrement by the new start_of_window
                - if start_of_window >= 0:
                    - current_ways_to_top -= ways_to_top[start_of_window]

            increment by the new end of the window
            - current_ways_to_top += ways_to_top[end_of_window]

            update the DS with the at the current_height with the current_ways_to_top
                - ways_to_top.append(current_ways_to_top)

    - Output(int): ways_to_top[height]
        the number of ways you can climb a staircase of a given height
		- return ways
'''
# Time: O(n) | # Space: O(n)
def staircaseTraversal(height, maxSteps):
    current_ways_to_top = 0
    ways_to_top = [1]

    for current_height in range(1, height + 1):
        start_of_window = current_height - maxSteps - 1
        end_of_window = current_height - 1

        if start_of_window >= 0:
            current_ways_to_top -= ways_to_top[start_of_window]

        current_ways_to_top += ways_to_top[end_of_window]
        ways_to_top.append(current_ways_to_top)

    return ways_to_top[height]


# Time: O(k * n) | # Space: O(n)
def staircaseTraversal_k_n_iteration(height, maxSteps):
    ways_to_top = []
    for height in range(height + 1):
        if height <= 1:
            ways_to_top.append(1)
            continue
        ways_to_top.append(0)

    for current_height in range(2, height + 1):
        step = 1
        ways = 0
        while step <= maxSteps and step <= current_height:
            ways += ways_to_top[current_height - step]
            step += 1
        ways_to_top[current_height] = ways
    return ways_to_top[height]


# Time: O(k * n) | # Space: O(n)
def staircaseTraversal_k_n_recursion(height, maxSteps):
    memoize = {0: 1, 1: 1}
    return ways_to_the_top(height, maxSteps, memoize)


'''
Algo Time: O() | # Space: O():
Main Function
- Input(int, int): height, maxSteps

we need create a DS that will store the number of ways_to_top for any given height
    this DS range should be 0 to the height of the staircase
    for the heights that are the base cases, height <= 1
        we can initalize those values
        - ways_to_top[0] = 1
        - ways_to_top[1] = 1

    to find the number of ways_to_top for the current height
        sum the last (height - maxSteps) elements in the data structure

        For each height in the range of 2 to the final height
        - for current_height in range(2, height + 1):

            for each previous step that is within the range of maxSteps
                increment ways by the current_height's ways_to_top - the step
                increment step by 1
            - while step <= maxSteps and step <= current_height:
                - ways += ways_to_top[current_height - step]
                - step += 1

            update the DS with the at the current_height with the ways
                - ways_to_top[current_height] = ways

    - Output(int): ways_to_top[height]
        the number of ways you can climb a staircase of a given height
		- return ways
'''
def ways_to_the_top(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]

    ways = 0
    for step in range(1, min(maxSteps, height) + 1):
        ways += ways_to_the_top(height - step, maxSteps, memoize)

    memoize[height] = ways
    return ways


# Time: O(k^n) | # Space: O(n)
def staircaseTraversal_k_to_the_n(height, maxSteps):
    return ways_to_top(height, maxSteps)


'''
Algo Time: O(k^n) | # Space: O(n)
Recursive Function
    - Input(int, int): height, maxSteps
		Base Case
            if the height is less than or equal to 1, then we know the ways_to_top is 1
            - return 1
        the ways variable will store the number of ways_to_top for a given height
            start the increment at zero.
            - ways = 0
        for each step within the range of max steps from the final step
            increment number of ways
            - for step in range(1, min(maxSteps, height) + 1):
                - ways += ways_to_top(height - step, maxSteps)

    - Output(int): ways
        the number of ways you can climb a staircase of a given height
		- return ways
'''
def ways_to_top(height, maxSteps):
    if height <= 1:
        return 1

    ways = 0
    for step in range(1, min(maxSteps, height) + 1):
        ways += ways_to_top(height - step, maxSteps)

    return ways


height = 4
maxSteps = 2
print("height:", height)
print("maxSteps:", maxSteps)
print("staircaseTraversal_k_to_the_n:",
      staircaseTraversal_k_to_the_n(height, maxSteps))
print("staircaseTraversal_k_n_recursion:",
      staircaseTraversal_k_n_recursion(height, maxSteps))
print("staircaseTraversal_k_n_iteration:",
      staircaseTraversal_k_n_iteration(height, maxSteps))
print("staircaseTraversal_n:", staircaseTraversal(height, maxSteps))
print(" ")

height = 100
maxSteps = 1
print("height:", height)
print("maxSteps:", maxSteps)
print("staircaseTraversal_k_to_the_n:",staircaseTraversal_k_to_the_n(height, maxSteps))
print("staircaseTraversal_k_n_recursion:",staircaseTraversal_k_n_recursion(height, maxSteps))
print("staircaseTraversal_k_n_iteration:",staircaseTraversal_k_n_iteration(height, maxSteps))
print("staircaseTraversal_n:", staircaseTraversal(height, maxSteps))
print(" ")


height = 1
maxSteps = 1
print("height:", height)
print("maxSteps:", maxSteps)
print("staircaseTraversal_k_to_the_n:", staircaseTraversal_k_to_the_n(height, maxSteps))
print("staircaseTraversal_k_n_recursion:", staircaseTraversal_k_n_recursion(height, maxSteps))
print("staircaseTraversal_k_n_iteration:", staircaseTraversal_k_n_iteration(height, maxSteps))
print("staircaseTraversal_n:", staircaseTraversal(height, maxSteps))
print(" ")