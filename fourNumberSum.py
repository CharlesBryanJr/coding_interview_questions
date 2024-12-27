'''fourNumberSum.py'''
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

Input(array, targetSum):
# Intuitive
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

Observations / Clarifying Questions / Insights:
# distinct integers
# quadruplets == a pair of two numbers


Output(array): four_number_sum_array
# a 2D array of four_number_sum quadruplets
'''

'''
# Time: O(n^2) | # Space: O(n^2)
Main Function
Input(array, targetSum):


To solve the fourNumberSum problem, a few observations need to be made.

1. The fourNumberSum problem can be reduced to the twoNumberSum problem.
    # pair two numbers together, their sum can be analyzed as a single number.  
3. Understand how to add addition values to a key in a dictionary
    # for each key, create the values as a 2D array
    # when addition values need to be added to a key, append the addition values
2. Understand how to avoid duplicates
    # only add a key & value to a dictionary
    # at the last occurence/opportunity to create the key & value
    # or
    # add to a key's values in a dictionary
    # at the last occurence/opportunity to add to the key's values



create an array named four_number_sum_array
    # four_number_sum_array will store each quadruplets that sums to the targetSum
    # once a quadruplet of numbers that sums to the targetSum is identified 
        # append the quadruplet to the array

create an hash table named pair_sums_dict
    # pair_sums_dict will used to search for complementary pair of numbers that sum to the targetSum
    # the keys will be the sum, of each pair of numbers, in the key's value array
    # the values will be an array of, pairs of numbers, that sum to the key
    # complementary pair of numbers


iterate through the entire array, starting from idx == 0
# this loop will used to iterate through all indices

    create a variable named num
        # num will store the current number in the array 

    iterate to the end of the array,
    starting from the index + 1 of the outer index
        # this loop will used to iterate through future indices

        create a variable named right_num
            # right_num will store the num of future numbers in the array

        create a variable named right_sum
            # right_sum will store the sum of the num and right_num
            # right_sum will be used to identify a complementary_sum that will sum to the targetSum

        create a variable named complementary_sum
            # complementary_sum will store the difference between targetSum and right_sum

            # if any other pairs of numbers sums up to the complementary_sum, 
            # then we have found a quadruplets that sum to the targetSum

            # complementary_sum will be used to retrieve,
            # all other pairs of numbers that sums up to complementary_sum
                # via lookup in the hashtable

        determine if the complementary_sum exist in pair_sums_dict hash table
            # if the complementary_sum exist,
            # then we have found quadruplets that sum to the targetSum

                iterate through each each pair of numbers,
                at the complementary_sum in the pair_sums_dict hash table
                    # each pair, will sum to the complementary_sum,
                    # and when added to the right_sum, will equal the targetSum

                    append the pair concatenated array of the num and right num
                        # we now need to add the quadruplet to the four_number_sum_array

                        # since the pair is already an array,
                        # we can just concatenate it with the num and right_num

            DO NOTHING
                # if the complementary_sum does NOT exist,
                    # either
                # the coresponding numbers in the array,
                # that sum to the complementary_sum,
                # have not been added
                    # or
                # the coresponding numbers that sum to the complementary_sum,
                # do not exist


    iterate to the beginning of the array,
    starting from the index - 1 of the outer index
        # this loop will used to iterate through past indices

        create a variable named left_num
            # left_num will store the num of past numbers in the array

        create a variable named left_sum
            # left_sum will store the sum of the num and left_num
            # left_sum will be used to either create a new key and value in the pair_sums_dict hash table
                # or
            # left_sum will be used to add to an existing key's values in the pair_sums_dict hash table

        determine if the left_sum exist in pair_sums_dict hash table
            # if the left_sum does NOT exist,
            # then we have found the first occurence of a pair of numbers,
            # that sum to that value

            create a new key and value in the pair_sums_dict hash table
                # the key will be the left_sum
                # the value will be a 2D array of the num and left_num
                    # the value needs to be a 2D array, 
                    # so additional pairs can be appended

            # if the left_sum does exist,
            # then we have an addition pair of numbers,
            # that add up to the same sum
                append the array of num and left_num,
                to left_sum's values in the pair_sums_dict hash table


Output(array): four_number_sum_array
# a 2D array of four_number_sum quadruplets
'''

# Time: O(n^2) | # Space: O(n^2)
def fourNumberSum_iteration(array, targetSum):
    four_number_sum_array = []
    pair_sums = {}
    for i in range(1, len(array)):
        for ii in range(i + 1, len(array)):
            currentSum = array[i] + array[ii]
            diff = targetSum - currentSum
            if diff in pair_sums:
                for pair in pair_sums[diff]:
                    four_number_sum = [pair[0], pair[1], array[i], array[ii]]
                    four_number_sum_array.append(four_number_sum)
        for iii in range(0, i):
            currentSum = array[i] + array[iii]
            pair = [array[i], array[iii]]
            if currentSum not in pair_sums:
                pair_sums[currentSum] = [pair]
            else:
                pair_sums[currentSum].append(pair)

    return four_number_sum_array


# _recursion
# _iteration
def fourNumberSum_recursion(array, targetSum):
    return get_four_number_sum(1, targetSum, array, {}, [])

def get_four_number_sum(mid, targetSum, array, pair_sums, four_number_sum_array):
    if mid >= len(array) - 1:
        return four_number_sum_array

    is_four_number_sum(mid, mid + 1, targetSum, array, pair_sums, four_number_sum_array)
    add_pair(0, mid, targetSum, array, pair_sums, four_number_sum_array)

    return get_four_number_sum(mid + 1, targetSum, array, pair_sums, four_number_sum_array)

def is_four_number_sum(mid, right, targetSum, array, pair_sums, four_number_sum_array):
    if right >= len(array):
        return

    currentSum = array[mid] + array[right]
    diff = targetSum - currentSum
    if diff in pair_sums:
        for pair in pair_sums[diff]:
            four_number_sum = [pair[0], pair[1], array[mid], array[right]]
            four_number_sum_array.append(four_number_sum)

    return is_four_number_sum(mid, right + 1, targetSum, array, pair_sums, four_number_sum_array)

def add_pair(left, mid, targetSum, array, pair_sums, four_number_sum_array):
    if left >= mid:
        return

    currentSum = array[left] + array[mid]
    pair = [array[left], array[mid]]
    if currentSum in pair_sums:
        pair_sums[currentSum].append(pair)
    else:
        pair_sums[currentSum] = [pair]

    return add_pair(left + 1, mid, targetSum, array, pair_sums, four_number_sum_array)


array = [7, 6, 4, -1, 1, 2]
targetSum = 16
print("array:", array)
print("targetSum:", targetSum)
print("fourNumberSum_iteration:", fourNumberSum_iteration(array, targetSum))
print("fourNumberSum_recursion:", fourNumberSum_recursion(array, targetSum))
print(" ")

array = [5, -5, -2, 2, 3, -3]
targetSum = 0
print("array:", array)
print("targetSum:", targetSum)
print("fourNumberSum_iteration:", fourNumberSum_iteration(array, targetSum))
print("fourNumberSum_recursion:", fourNumberSum_recursion(array, targetSum))
print(" ")


array = [1, 2, 3, 4, 5, -5, 6, -6]
targetSum = 5
print("array:", array)
print("targetSum:", targetSum)
print("fourNumberSum_iteration:", fourNumberSum_iteration(array, targetSum))
print("fourNumberSum_recursion:", fourNumberSum_recursion(array, targetSum))
print(" ")

