'''minRewards.py'''
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
-

Type of Question:
- Array
		- draw indices
		- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values
		- running sums
		- sliding windows
			- start_of_window
			- end_of_window

# Dictionaries (Hashmaps)
 # Understand how to add addition values to a key in a dictionary
    # for each key, create the values as a 2D array
    # when addition values need to be added to a key, append the addition values
	# Understand how to avoid duplicates
    # only add a key & value to a dictionary
    # at the last occurence/opportunity to create the key & value
    # or
    # add to a key's values in a dictionary
    # at the last occurence/opportunity to add to the key's values

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
	- 
- Graphs
	- traverse through the graph DFS or BFS
			- for NON connected graphs, loop over every node
			- create and use a visited DS to optimize
			- stack / queue
	- trie edge == leads to a new descendant node
		- create a visited DS and initalize with false
	- back edge == leads to an already discovered ancestor node
		- if a back edge is exists == cycle
		- if a node is on the recursion stack and we reach it again
		- if a node is on the recursion stack, it is the ancestor of the current node
		- create a in_stack DS and initalize with false
	# cross edge == leads from one descendant to another already discovered descendant in a different subtree
	# forward edge == leads to an already discovered descendant node
	# connected
     # zero island nodes
	# unweighted
		# the distance between all of the nodes is the exact same
	# undirected
        # travel in either direction
		# if a vertex appears in the edge list of another vertex (inverse will also be true)
		# if a vertex A is connected to vertex B, then vertex B is connected to Vertex A
# Greedy
	# 
# Heaps
# Linked List
	# keep track of node via temp variable
	# create a dummy node
# Recursion
	# the solution depends on solutions to smaller instances of the same problem
		# define the smaller instance of the problem
			# translate the for/while loop into a base case
	# will iterate/traverse until the function can return a value (base case)
		# always include return statment
	# base case == the smallest instance of the problem that can be solved directly
	# to keep track of element, store the element in a variable that connected to the recursion call
	# running variables left to right
			# arguments
	# running variables right to left
			# return statment
	# Recursive functions often take a sub array of the original array
	# the outcome of a recursive function will affect code on lines after it
	# To optimize use memoization
		# store the answer to recursive calls in a hash table
	# 1. Base Case
	# 2. Action
	# 3. update variables
	# 4. Recursion
		if idx >= len(array):


# Searching
# Sorting
# Stacks
# Strings
# Tries

Input():
# Intuitive
    # array of postive integers
# Primitive Types
		# Numbers
			# Zero (0)
			# NULL or nil
			# Negative Numbers
			# Floats or Doubles (clarifies if Ints only?)
			# Min/Max Int
		# Arrays
			# Empty array
			# Nested or not nested
		# Dictionaries (Hashmaps)
			# Collisions
		# Linked Lists (Stacks, Queues, Deques)
			# Circular
			# Loops (present or not?)
			# Doubly-Linked List

Observations / Clarifying Questions / Insights:
# every student gets a reward
# if the current num > a adjacent numbers,
    # the current idx should receive a greater reward
    # than the idx next to it with a lower num
# if the current num < a adjacent number,
    # the current idx should receive a lesser reward
    # than the idx next to it with a greater num
# return the min number of rewards needed to stafiy the other rules
# only unique integers
# the order matters == no sorting the array
# PEAKS and VALLEYS


Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output():

'''

'''
# Time: O(n^2) | # Space: O(n)
Main Function
Input(array): scores

rewards = []
# the rewards array will store the amount of reward,
# that a student has earned
#
# we will need to sum each reward,
# at the end of the algo,
# to calcuate the minimum rewards needed

for idx in range(len(scores)):
    rewards.append(1)
# initailze each student's idx,
# with a reward of 1,
#
# which is the minimum number of rewards,
# that a student can earn

for idx in range(1, len(scores)):
# to determine the min score for each student,
# we need to iterate from 1 to the end of the array
    # we can start at 1 because,
    # we will be executing a comparison between the,
    # current idx and the previous idx

    ii = i - 1
    # create a variable, ii,
    # that will store the previous idx,
    # for each iteration,
    # and, if needed,
    # will be decremented to zero,
    # if we need to fix previous scores,
    # already assigned

    last_score = scores[ii]
    score = scores[i]
    # create two variables, last_score and score
    # so that we can perform the compairson of the,
    # last score to the previous score

    if score > last_score:
    # determine if the current score is greater than,
    # the last score
        # if SO,
            last_reward = reward[ii]
            reward[i] = last_reward + 1
            # if the current score IS,
            # greater than,
            # the last score,
            # then we can just,
            # give the current student,
            # one more reward,
            # than the last student
        # if NOT
            # if the current score is NOT greater than,
            # the last score,

            reward[i] = 1
            # give the current student,
            # the smallest reward possible,
            # which is 1
            #

            left_score = left_score[ii]
            right_score = right_score[ii + 1]
            left_reward = rewards[ii]
            right_reward = rewards[ii + 1]

            # create four variables,
            # left_score and right_score,
            # and
            # left_reward and right_reward,
            #
            # so that we can perform a compairson of,
            # the already assigned adjacent scores,
            # that potenially are now incorrect,
            # due to the current student reward,
            # being assigned,
            # the smallest reward possible,
            # which is 1

            while ii >= 0 and left_reward > right_reward
            # because we want to give,
            # the current student,
            # the smallest reward possible,
            # which is 1,
            # we need check and update,
            # previously assigned rewards,
            # that will break a rule if left as is

            # to do so, iterate in reverse,
            # back to 0,
            # or
            # until the left_score is NOT,
            # greater than the right_score

                rewards[ii] = max(left_reward, right_reward + 1)
                # while the left score IS,
                # greater than the right_score,
                # the left_reward needs to be,
                # greater than the right_reward
                #
                # so, update the left_reward,
                # to be the MAX of the,
                # left_reward and the right_reward + 1
                #
                    # if the left_reward is alreadly,
                    # greater than the right_reward + 1,
                    # then the left_reward,
                    # is greater than the right_reward
                    # so the rules to the right,
                    # are satisfied
                    #
                    # the rules to the left,
                    # are already satisfied,
                    # since, the left_reward is already,
                    # correctly assigned a reward amount,
                    # in relation to the,
                    # left_reward's left_reward
                    #
                    # SO, do nothing
                    #
                    # if the left_reward is less than the,
                    # right_reward + 1,
                    # then, the left_reward is NOT,
                    # greater than the right_reward.
                    # which breaks the rules to the right.
                    #
                    # So, update the left_reward,
                    # to be equal to right_reward + 1,
                    # which will make the left_reward,
                    # greater than the right_reward,
                    # and satisfy the rules to the right

#

Output(int): min_rewards
# the minimum sum of all the rewards given to each student
'''

# Time: O(n^2) | # Space: O(n)
def minRewards_n_n(scores):
    rewards = []
    for idx in range(len(scores)):
        rewards.append(1)

    for i in range(1, len(scores)):
        ii =  i - 1
        if scores[i] > scores[ii]:
            rewards[i] = rewards[ii] + 1
        else:
            ii =  i - 1
            while ii >= 0 and scores[ii] > scores[ii + 1]:
                if rewards[ii + 1] + 1 > rewards[ii]:
                    rewards[ii] = rewards[ii + 1] + 1
                #rewards[ii] = max(rewards[ii], rewards[ii + 1] + 1)
                ii -= 1

    return sum(rewards)


'''
# Time: O(n) | # Space: O(n)
Main Function
Input(array): scores

# PEAKS and VALLEYS solution

rewards = []
# the rewards array will store the amount of reward,
# that a student has earned
#
# we will need to sum each reward,
# at the end of the algo,
# to calcuate the minimum rewards needed

for idx in range(len(scores)):
    rewards.append(1)
# initailze each student's idx,
# with a reward of 1,
#
# which is the minimum number of rewards,
# that a student can earn


local_minimums_idxs = find_local_minimum_idxs(scores)
# the local_minimums_idxs array will store the indices,
# of the local minimum scores in the scores array.
# we will initalize this local_minimums_idxs array, 
# with the return object of the,
# find_local_minimum_idxs function
    # we need to locate the local minimum scores,
    # in the scores array,
    # local valleys should be assigned,
    # the value of 1,
    # because their reward,
    # needs to be smaller than,
    # their adjacent values 
    # and 
    # we want to give any student possible, 
    # the minimum rewards possible, which is 1


for local_min_idx in local_minimums_idxs:
# now that we have identified and stored,
# the local_min_idxs in the local_minimums_idxs array
# iterate through the local_minimums_idxs array,
# to identify the starting point of the,
# expand_left_from_local_min 
# and 
# expand_right_from_local_min 
# functions
    expand_left_from_local_min(local_min_idx, scores, rewards)
    expand_right_from_local_min(local_min_idx, scores, rewards)
    # for each function call,
    # pass the current local_min_idx we are exploring
    # pass the scores array,
        # o we can
    # pass the rewards array, 
        # so we can read and update
        # the array as necessary 

Output(int): min_rewards
# the minimum sum of all the rewards given to each student

def find_local_minimum_idxs(array):
# to solve this problem, 
# we need to find_local_minimum_idxs,
# because, 
# if we know where the local minimums are,
# we can assign local minimums the smallest value possible
# and 
# we can expand left and right from local minimums,
# and assign rewards with the ref
#
# this function will return the local_minimums_indices,
# found in the array,

    if len(array) == 1:
        return [0]
    # be default, if the length of the array is 1, 
    # the the single element is the local min

    local_minimums_idxs = []
    # the local_minimums_idxs array will store the indices,
    # of the local minimum scores in the scores array.
    # initalize local_minimums_idxs array with nothing,
    # as we find local minimums, 
    # we will append the to this array

    for i in range(len(array)):
    # to add local_min_idx to the local_minimums_idxs array,
    # we need to identify local minimums in the array
    # so, we need to loop through the entire array, 
    # starting from 0 to the end of the array

        if i == 0 and array[i] < array[i + 1]:
        # for the edge case of when the iterator,
        # is at index 0,
        # a left_idx will not exist,
        # so, we only need to check the right idx,
        # to determine if the 0th index is a local min

            if SO, local_minimums_idxs.append(i)
                # then the 0th index is a local min
                # and we need to add it's index to the
                # local_minimums_idxs array
        
        if i == len(array) - 1 and array[i] < array[i - 1]:
        # for the edge case of when the iterator,
        # is at the last index in the array,
        # a right_idx will not exist,
        # so, we only need to check the left idx,
        # to determine if the last index is a local min

            if SO, local_minimums_idxs.append(i)
                # then the last index is a local min
                # and we need to add it's index to the
                # local_minimums_idxs array
        
        if i == 0 or i == len(array) - 1:
            continue
        # in the edge case where, 
        # i is at the beginning or end of the array,
        # and we already performed our,
        # check and appended of the idx,
        # if we could, 
        # then we need to continue to the next iteration
        #
            # note, seperating this continue action,
            # from the orginal check and append,
            # we can handle the cases where,
            # we are at the edges of the array 
            # but 
            # they were not local minimums 
            # and we would never jump inside,
            # of the if statement
        
        if array[i] < array[i - 1] and array[i] > array[i + 1]
            # at this point, 
            # we know that the iterator is in the middle,
            # of the array
            # so,
            # we need to check both the left and right values
            # to determine if the idx is a local minimum
            
            if SO, local_minimums_idxs.append(i)
                # then the index is a local min
                #we need to add to the
                # local_minimums_idxs array

                

def expand_left_from_local_min(local_min_idx, scores, rewards)
# given a local_min_idx,
# the expand_left_from_local_min function will
# read/update/assign rewards to students, 
# that have lower idex value,
# then the local min 
    # this function is needed to correct assign rewards,
    # to students in the rewards array

    idx = local_min_idx - 1
    # create a variable, idx,
    # to store the current idx,
    # 
    # this value will be decremented,
    # every iteration because we want to 
    # expand to the left
    # 
    # initialze idx with the value of,
    # the local_min_idx - 1,
    # because we want to start the expanison from the,
    # local_min_idx's left_idx

    while idx >= 0 and scores[idx] > scores[idx + 1]:
    # itereate from the idx to zero,
    # while the the score,
    # is greater than the score to the right of it
    # 
    # this comparison of the score and the right score,
    # will identify a local peak of the scores array,
    # because if the score is less than the right score,
    # then a peak has been found,
    # and we want to stop the loop

        rewards[idx] = max(rewards[idx], rewards[idx + 1] + 1)
        # because, the loop would break, 
        # if the score is less than the right score,
        # we know, the score is greater than,
        # the right score and therefore,
        # the reward, should be greater than the right,
        # reward
        #
        # because the reward, 
        # is already correct assigned,
        # in relation to the reward's left_reward,
        # when the new constraint of the the reward,
        # needing to be greater than,
        # the right_reward develops, 
        # we need to increase the reward,
        # if it is not greater than the right reward

        idx -= 1
        # decrement the idx so the loop continues



def expand_right_from_local_min(local_min_idx, scores, rewards)
# given a local_min_idx,
# the expand_right_from_local_min function will
# read/update/assign rewards to students, 
# that have HIGHER idex value,
# then the local min 
    # this function is needed to correct assign rewards,
    # to students in the rewards array

    idx = local_min_idx + 1
    # create a variable, idx,
    # to store the current idx,
    # 
    # this value will be incremented,
    # every iteration because we want to 
    # expand to the right
    # 
    # initialze idx with the value of,
    # the local_min_idx + 1,
    # because we want to start the expanison from the,
    # local_min_idx's right_idx

    while idx < len(scores) and scores[idx] > scores[idx - 1]:
    # itereate from the idx to the end of the array,
    # while the the score,
    # is greater than the score to the left of it
    # 
    # this comparison of the score and the left score,
    # will identify a local peak of the scores array,
    # because if the score is less than the left score,
    # then a peak has been found,
    # and we want to stop the loop

        rewards[idx] = max(rewards[idx], rewards[idx + 1] + 1)
        # because, the loop would break, 
        # if the score is less than the left score,
        # we know, the score is greater than,
        # the left score and therefore,
        # the reward, should be greater than,
        # the left reward
        #
        # because the reward, 
        # is already correct assigned,
        # in relation to the reward's left_reward,
        # when the new constraint of the the reward,
        # needing to be greater than,
        # the left_reward develops, 
        # we need to increase the reward 
        # to be one greater that the left_reward
            # one greater is the minimum reward,
            # this student could earn    

        idx += 1
        # increment the idx so the loop continues
'''

# Time: O(n) | # Space: O(n)
def minRewards_n_iteration(scores):
    rewards = []
    for idx in range(len(scores)):
        rewards.append(1)

    local_min_idxs = find_local_min_idxs_iteration(scores)

    for local_min_idx in local_min_idxs:
        expand_left_from_local_min(local_min_idx, scores, rewards)
        expand_right_from_local_min(local_min_idx, scores, rewards)

    return sum(rewards)

def find_local_min_idxs_iteration(array):
    if len(array) == 1:
        return [0]

    local_min_idxs = []

    for idx in range(len(array)):

        if idx == 0 and array[idx] < array[idx + 1]:
            local_min_idxs.append(idx)

        if idx == len(array) - 1 and array[idx] < array[idx - 1]:
            local_min_idxs.append(idx)

        if idx == 0 or idx == len(array) - 1:
            continue

        if array[idx] < array[idx - 1] and array[idx] < array[idx + 1]:
            local_min_idxs.append(idx)

    return local_min_idxs

def expand_left_from_local_min(local_min_idx, scores, rewards):
    for idx in reversed(range(local_min_idx)):
        if scores[idx] > scores[idx + 1]:
            if rewards[idx + 1] + 1 > rewards[idx]:
                rewards[idx] = rewards[idx + 1] + 1

def expand_right_from_local_min(local_min_idx, scores, rewards):
    for idx in range(local_min_idx + 1, len(scores)):
        if scores[idx] > scores[idx - 1]:
            if rewards[idx - 1] + 1 > rewards[idx]:
                rewards[idx] = rewards[idx - 1] + 1


# Time: O(n) | # Space: O(n)
def minRewards_n_recursion(scores):
    rewards = []
    for idx in range(len(scores)):
        rewards.append(1)

    local_min_idxs = find_local_min_idxs_recursion(scores)

    for local_min_idx in local_min_idxs:
        expand_left_from_local_min_recursion(local_min_idx - 1, scores, rewards)
        expand_right_from_local_min_recursion(local_min_idx + 1, scores, rewards)

    return sum(rewards)


def find_local_min_idxs_recursion(array):
    if len(array) == 1:
        return [0]

    local_min_idxs = []

    if array[0] < array[1]:
        local_min_idxs.append(0)

    if array[len(array) - 1] < array[len(array) - 1 - 1]:
        local_min_idxs.append(len(array) - 1)

    is_local_min_idxs(1, local_min_idxs, array)

    return local_min_idxs

def is_local_min_idxs(idx, local_min_idxs, array):
    if idx >= len(array) - 1:
        return

    if array[idx] < array[idx - 1] and array[idx] < array[idx + 1]:
        local_min_idxs.append(idx)
    
    is_local_min_idxs(idx + 1, local_min_idxs, array)

def expand_left_from_local_min_recursion(idx, scores, rewards):
    if idx < 0:
        return

    if scores[idx] > scores[idx + 1]:
        if rewards[idx + 1] + 1 > rewards[idx]:
            rewards[idx] = rewards[idx + 1] + 1

    expand_left_from_local_min_recursion(idx - 1, scores, rewards)

def expand_right_from_local_min_recursion(idx, scores, rewards):
    if idx >= len(scores):
        return

    if scores[idx] > scores[idx - 1]:
        if rewards[idx - 1] + 1 > rewards[idx]:
            rewards[idx] = rewards[idx - 1] + 1

    expand_right_from_local_min_recursion(idx + 1, scores, rewards)

'''
# Time: O(n) | # Space: O(n)
Main Function
Input(array): scores

# the expansion techinque used in the last solution,
# can be applied without finding the local mins,

# from any idx greater than 1 to the end of the array,
    # if the current score is greater than the last score,
    # then the current reward must be greater than the 
    # last reward

for idx in range(1, len(scores)):
    if scores[idx] > scores[idx - 1]:
        rewards[idx] = rewards[idx - 1] + 1

# using the two concpet above, we can expand right,
# and update the current reward to be one greater than the,
# last reward any time the current score is greater than the,
# last score


# from any idx less than the end of the array
# and greater than - 1,
    # if the current score is greater than the last score,
    # then the current reward must be greater than the 
    # last reward

for idx in reversed(range(len(scores) - 1)):
    if scores[idx] > scores[idx + 1]:
        if rewards[idx + 1] + 1 > rewards[idx]:
            rewards[idx] = rewards[idx + 1] + 1

# using the two concpet above, we can expand left,
# and update the current reward to be one greater than the,
# last reward any time the current score is greater than the,
# last score


rewards = []
# the rewards array will store the amount of reward,
# that a student has earned
#
# we will need to sum each reward,
# at the end of the algo,
# to calcuate the minimum rewards needed

for idx in range(len(scores)):
    rewards.append(1)
# initailze each student's idx,
# with a reward of 1,
#
# which is the minimum number of rewards,
# that a student can earn


Output(int): min_rewards
# the minimum sum of all the rewards given to each student
'''

# Time: O(n) | # Space: O(n)
def minRewards_iteration(scores):
    rewards = []
    for idx in range(len(scores)):
        rewards.append(1)

    for idx in range(1, len(scores)):
        if scores[idx] > scores[idx - 1]:
            rewards[idx] = rewards[idx - 1] + 1

    for idx in reversed(range(len(scores) - 1)):
        if scores[idx] > scores[idx + 1]:
            if rewards[idx + 1] + 1 > rewards[idx]:
                rewards[idx] = rewards[idx + 1] + 1

    return sum(rewards)

# Time: O(n) | # Space: O(n)
def minRewards_recursion(scores):
    rewards = [1 for reward in scores]
    expand_right(1, scores, rewards)
    expand_left(len(scores) - 2, scores, rewards)
    return sum(rewards)


def expand_right(idx, scores, rewards):
    if idx >= len(scores):
        return
    if scores[idx] > scores[idx - 1]:
        rewards[idx] = rewards[idx - 1] + 1
    expand_right(idx + 1, scores, rewards)


def expand_left(idx, scores, rewards):
    if idx < 0:
        return
    if scores[idx] > scores[idx + 1]:
        if rewards[idx + 1] + 1 > rewards[idx]:
            rewards[idx] = rewards[idx + 1] + 1
    expand_left(idx - 1, scores, rewards)


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print("scores:", scores)
print("minRewards_n_n:", minRewards_n_n(scores))
print("minRewards_n_iteration:", minRewards_n_iteration(scores))
print("minRewards_n_recursion:", minRewards_n_recursion(scores))
print("minRewards_iteration:", minRewards_iteration(scores))
print("minRewards_recursion:", minRewards_recursion(scores))
print(" ")

scores = [0, 4, 2, 1, 3]
print("scores:", scores)
print("minRewards_n_n:", minRewards_n_n(scores))
print("minRewards_n_iteration:", minRewards_n_iteration(scores))
print("minRewards_n_iteration:", minRewards_n_iteration(scores))
print("minRewards_iteration:", minRewards_iteration(scores))
print("minRewards_recursion:", minRewards_recursion(scores))
print(" ")

scores = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
print("scores:", scores)
print("minRewards_n_n:", minRewards_n_n(scores))
print("minRewards_n_iteration:", minRewards_n_iteration(scores))
print("minRewards_n_iteration:", minRewards_n_iteration(scores))
print("minRewards_iteration:", minRewards_iteration(scores))
print("minRewards_recursion:", minRewards_recursion(scores))
print(" ")