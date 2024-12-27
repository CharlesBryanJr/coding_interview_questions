'''largestRange.py'''
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


Input(array): array
# Intuitive
    # array of integers
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

Observations / Clarifying Questions / Insights:
# range of numbers
    # set of numbers that come right after each other,
    # in the set of real integers
    #
# numbers do not need to be sorted to form a range
# numbers do not need to be adjacent to form a range
# only one largest range
# any given number can only be involved in one range

Output(array): output
# array of length 2
# representing the largest range of integers contained in that array
# output[0] == the first number in the range
# output[1] == the last number in the range
'''

# Time: O(nlog(n)) | # Space: O(1)
def largest_range(array):
    array.sort()
    start = array[0]
    end = array[0]

    largest_range_array = [start, end]
    largest_range_count = 0

    range_count = 0

    for idx in range(1, len(array)):
        last_num = array[idx - 1]
        num = array[idx]

        if num == last_num:
            continue

        if num == last_num + 1:
            range_count += 1
            end = array[idx]
            continue

        if range_count > largest_range_count:
            largest_range_count = range_count
            largest_range_array = [start, end]

        start = array[idx]
        end = array[idx]
        range_count = 0

    if range_count > largest_range_count:
        largest_range_array = [start, end]

    return largest_range_array


'''
# Time: O(n) | # Space: O(n)
Main Function
Input(array): array

To improve our time complexity from nlogn to n, 
we will need to expand our space complexity.

By sorting the array, all that was needed 
to determine if a range was "ongoing/active",
was a comparison of the comparison of 
the last number and the current number.

Without sorting the array, 
we still need to be able to count range lengths. 
Since, the adjacent numbers are not in ascending order,
we need to create a set, 
to store all numbers 
and determine if the next number in a given range,
exist in the input array.

Once the set is created, 
we can iterate from the smallest value to largest value.
This will allow us to check if the,
current num and it's adjacent numbers,
exist in the set.
If the the current num and it's adjacent numbers exist, 
then we found a range 
and we want to count the this range.

create a set and add all numbers in the input array to the set
    # this set will all us to store all numbers,
    # in the input array
    # and 
    # determine a range of possible numbers in the set.

create two variables, smallest_value and largest_value
    smallest_value == the smallest value in the set/input array
    largest_value == the largest value in the set/input array

    # these two variables, 
    # are the start and end,
    # of the range of number we need to loop through.

create two variables, start and end,
initalize with them to equal the smallest_value
    # these two variables will store 
    # the start value and end value  
    # of the largest range

create the output array, largest_range_array
that will return the largest range
initalize with the start and end variables

create the variable, largest_range_count
which will store the the size of the the largest range
initalize with 0

for idx in range(smallest_value + 1, largest_value + 1):
    last_num = idx - 1
    num = idx

iterate through the range of 
the smallest_value + 1 
to
the largest_value + 1
    # this loop will iterate through all of the 
    # possible numbers that could be in the set

    last_num = idx - 1
    num = idx
    for each iteration, 
    update the varaibles last_num and num
        # these two variables will store,
        # adjacent numbers
        # and 
        # allow us to determine if 
        # a range is "ongoing/active"
    
    determine if last_num and num,
    exist in the set/input array
        # before we check if a range is "ongoing/active",
        # we need to verify if the two possible numbers, 
        # last_num and num, 
        # exist in the set/input array

        if last_num and num, 
        do exist in the set/input array
            # then we have an "ongoing/active" range

            update all varaibles that relate to,
            an "ongoing/active" range

        if last_num and num, 
        do NOT exist in the set/input array
            # this indicates that the current range is "broken/inactive"
            
            determine if the current range count is greater the the largest_range_count
                if so, 
                update largest_range_count == range_count
                and 
                update largest_range_array == [start, end]
                    # we have found a new largest_range_count
                    # and so,
                    # we need update largest_range_count for future iterations
                    # and update largest_range_array,
                    # to be the current start and end variables
                
                
                if not, do nothing
                # since we only care about the largest_range_count,
                # we do not need to take action on 
                # range_counts smaller than or equal to 
                # the largest_range_count
            
            reset all varaibles that relate to,
            an "ongoing/active" range    
 

    determine if the current range count is greater the the largest_range_count
        # to handle the edge case where the last number,
        # in the possible numbers that could be in the set,
        # contributes to the current range
        # and 
        # the current current range count is greater than 
        # the largest_range_count

        if so, 
        update largest_range_count == range_count
        and 
        update largest_range_array == [start, end]
            # we have found a new largest_range_count
            # and so,
            # we need update largest_range_count for future iterations
            # and update largest_range_array,
            # to be the current start and end variables


Output(array): largest_range_array
# array of length 2
# representing the largest range of integers contained in that array
# output[0] == the first number in the range
# output[1] == the last number in the range
# '''

# Time: O(n) | # Space: O(n)
def largestRange_n(array):
    range_set = {array[0]}
    for idx in range(1, len(array)):
        num = array[idx]
        range_set.add(num)

    smallest_value = min(range_set)
    largest_value = max(range_set)

    start = smallest_value
    end = smallest_value

    largest_range_array = [start, end]
    largest_range_count = 0

    range_count = 0

    for idx in range(smallest_value + 1, largest_value + 1):
        last_num = idx - 1
        num = idx

        if last_num in range_set and num in range_set:
            range_count += 1
            end = num
            continue

        if range_count > largest_range_count:
            largest_range_count = range_count
            largest_range_array = [start, end]

        start = idx
        end = idx + 1
        range_count = 0

    if range_count > largest_range_count:
        largest_range_array = [start, end]

    return largest_range_array


'''
# Time: O(n) | # Space: O(n)
Main Function
Input(array): array

To improve our time complexity from nlogn to n, 
we will need to expand our space complexity.

By sorting the array, all that was needed 
to determine if a range was "ongoing/active",
was a comparison of the comparison of 
the last number and the current number.

Without sorting the array, 
we still need to be able to count range lengths. 
Since, the adjacent numbers are not in ascending order,
we need to create a dict, 
to store all numbers 
and determine if the next number in a given range,
exist in the input array.

numbers = {}
# dictionary to store all the numbers in the input array

largest_range_array = []
# output array of the largest range of 
# consecutive ascending numbers 
# found in the input array

largest_range = 0
# used to store the lenfth of the largest_range
# and 
# identify if a current range_length is now the largest_range

for num in array:
    numbers[num] = True
# iterate through each number in the input array,
    # add the number to the dictonary 
    # and
    # set each num's value to False.
    #
    # a False value indicates that this number's potenital range,
    # has not been explored or counted.

for num in array:
# iterate through each number in the input array,
    
    if numbers[num] is False:
        continue
    # lookup if the current number has a value of False,
    # in the numbers dictionary
        # if so, continue to the next iteration
        # 
        # if a number has a value of False in the numbers dictionary,
        # then, that number's potenital range,
        # has been explored and counted,
        # so, we dont not need to recount it

    range_length = 1
    left = num - 1
    right = num + 1
    # if the current number has a value of NOT False,
    # in the numbers dictionary
    # then, the current number's potenital range,
    # has NOT been explored and counted, 
    # so it's time to do that now
    #
    # start the current range_length counter at 1
        # any number represents a length of 1
    # to explore the potential range that occurs,
    # before the current number,
    # we set left = number - 1

    # to explore the potential range that occurs,
    # after the current number,
    # we set right = number + 1


    while left in numbers:
        numbers[left] = False
        range_length += 1
        left -= 1
    
    # to explore the potential range that occurs,
    # BEFORE the current number
    #
    # iterate through every number from the left to -inf
        # for each number that exist in the numbers dictonary,
        # then we have found an additon number that contributes to,
        # the current numbers range
        # 
        # so, increment the current range_length by 1
        # and decrement left by 1 to go to the lesser value
        # 
        # also, set the left's value,
        # in the the numbers dictonary, to False
        #
        # this will prevent us from recounting the range that,
        # left's value contributes to
    

    while right in numbers:
        numbers[right] = False
        range_length += 1
        right += 1

    # to explore the potential range that occurs,
    # AFTER the current number
    #
    # iterate through every number from the right to +inf
        # for each number that exist in the numbers dictonary,
        # then we have found an additon number that contributes to,
        # the current numbers range
        # 
        # so, increment the current range_length by 1
        # and decrement left by 1 to go to the lesser value
        # 
        # also, set the right's value,
        # in the the numbers dictonary, to False
        #
        # this will prevent us from recounting the range that,
        # right's value contributes to

    if range_length > largest_range:
        largest_range = range_length
        largest_range_array = [left + 1, right - 1]
    
    # once we have finshed counting the current numbers range length,
    # then we need to check if the current numbers range length,
    # is the new longest range
        # if so, we want to update the varaible largest_range,
        # for future iterations
        # and
        # update our output array, largest_range_array
        # to reflect the new longest_range
            # note, that the current left and right value,
            # is not in the input array
            # 
            # left was decremented to the first number,
            # before the range of the current number
            #
            # so we add one to left, 
            # when assigning the start of the range,
            # in the output array

            # right was incremented to the first number,
            # after the range of the current number
            #
            # so we subtract one from right, 
            # when assigning the end of the range,
            # in the output array

        # if not, do nothing
        # if a range length is not longer than our largest range length,
        # we do not care about it,
        # and there is no action to take


Output(array): largest_range_array
# array of length 2
# representing the largest range of integers contained in that array
# output[0] == the first number in the range
# output[1] == the last number in the range
'''

# Time: O(n) | # Space: O(n)
def largestRange(array):
    numbers = {}
    largest_range_array = []
    largest_range = 0

    for num in array:
        numbers[num] = True

    for num in array:
        if numbers[num] is False:
            continue

        range_length = 1
        left = num - 1
        right = num + 1

        while left in numbers:
            numbers[left] = False
            range_length += 1
            left -= 1

        while right in numbers:
            numbers[right] = False
            range_length += 1
            right += 1

        if range_length > largest_range:
            largest_range = range_length
            largest_range_array = [left + 1, right - 1]

    return largest_range_array


'''
# Time: O(n) | # Space: O(n)
Main Function
Input(array): array

To improve our time complexity from nlogn to n, 
we will need to expand our space complexity.

By sorting the array, all that was needed 
to determine if a range was "ongoing/active",
was a comparison of the comparison of 
the last number and the current number.

Without sorting the array, 
we still need to be able to count range lengths. 
Since, the adjacent numbers are not in ascending order,
we need to create a dict, 
to store all numbers 
and determine if the next number in a given range,
exist in the input array.

numbers = {}
# dictionary to store all the numbers in the input array

start = array[0]
end = array[0]
# start and end will store the start and end,
# of the largest range of consecutive ascending numbers
#
# initalize both with the first value in the array,
# because, potenially, the array could be of size 1,
# and the largest range will be just that one number 

largest_range_array = []
# output array of the largest range of 
# consecutive ascending numbers 
# found in the input array

add_numbers(0, array, numbers)
# call the recursive function, add_numbers,
# which will create a new key and value,
# in the numbers dictionary
    # each number will be key
    # and every key will have the same value of false
    # a False value indicates that this number's potenital range,
    # has not been explored or counted.


largest_range_array = count_range_length(0, 0, start, end, array, numbers)
# call the recursive function, count_range_length,
# which will return the largest range of 
# consecutive ascending numbers 
# found in the input array
# 
# to store the output of count_range_length,
# return the result to a varaible, largest_range_array


Output(array): largest_range_array
# array of length 2
# representing the largest range of integers contained in that array
# output[0] == the first number in the range
# output[1] == the last number in the range




def add_numbers(idx, array, numbers):
# the parameters for this recursive function are, 
# the current idx, the array, and the numbers dictionary

    if idx >= len(array):
        return
    # each recursive function call, 
    # will check if the base case,
    # has been acheived
        # the base case is when the idx is,
        # equal to or larger than,
        # the size of the array,
        # if so, return None, back up the stack
            # since the numbers dictionary exists, 
            # outside of the recursive function,
            # each recursive function call, 
            # updates the "global" numbers dictionary
            # 
            # so, we do not need to return anything up the stack
        # if not, jump to the next line of code
    
    num = array[idx]
    # we create the varaible, num,
    # to store the current number that,
    # the current idx in the array holds.
    
    numbers[num] = True
    # we use the num varaible,
    # to create a new key in the numbers dictionary
    # and we set the value to True
        # if a key's value is True,
        # that indicates that the key, which is a number,
        # potenial range has not be explored or counted.

    add_numbers(idx + 1, array, numbers)
    # we then call the recursive function, add_numbers,
    # which is the recursive call that will create a loop
    #
    # for each iteration of the recursive function, 
    # we need to increment the index,
    # so we can perform the same function,
    # on a different index in the array
    # and eventually reach our base case



def count_range_length(idx, largest_range, start, end, array, numbers):
# the parameters for this recursive function are, 
# idx: the current idx, 
    # incremented each recursive function call
# largest_range:
    # the largest range of consecutive ascending numbers
    # each recursive function call, 
    # has the opporunity to update largest_range,
    # which is a "global" variable, 
    # that will be passed to the next,
    # recursive function call
        # regardless of an update or not
        # this will a running variable 
# start:
    # will store the start of the largest range of,
    # consecutive ascending numbers
# end
    # will store the end of the largest range of,
    # consecutive ascending numbers
# array: 
    # the input array
# numbers:
    #  the dictionary that stores all the numbers,
    #  all the numbers from the input array, 
    #  and, will allow us to check if,
    #  the current idx and corresponding number's,
    #  potenial range has been explored/counted

if idx >= len(array):
    return [start, end]
# each recursive function call, 
# will check,
# if the base case has been acheived
    # the base case is when,
    # the idx is equal to or larger than,
    # the size of the array,
    # if so, return [start, end], back up the stack
        # each recursive function call, 
        # has the opporunity to update start and end,
        # which are "global" variables, 
        # that will be passed to the next,
        # recursive function call
        #
        # so, once we have visited each idx in the array,
        # the value of start and end,
        # will be the desired output
    # if not, jump to the next line of code

num = array[idx]
# we create the varaible, num,
# to store the current number that,
# the current idx in the array holds.


if numbers[num] is True:
# lookup if the current number has a value of True,
# in the numbers dictionary
    # if so, that number's potenital range,
    # has NOT been explored and counted,
    # so, it's time to count it now

    numbers[num] = False
    # to prevent us from recounting this number's,
    # potenital range again, 
    # set this number's value to False


    range_length = 1
    # since it's time to start counting,
    # this number's potential range,
    # we can use the variable, range_length,
    # to store the length of the number's range
        # intialize range_length at 1,
        # any number represents a length of 1
    
    left = num - 1
    # to explore the potential range that occurs,
    # before the current number,
    # we set left = number - 1

    right = num + 1
    # to explore the potential range that occurs,
    # after the current number,
    # we set right = number + 1

    left_count = count_left(0, left, numbers)
    # to explore the potential range that occurs,
    # BEFORE the current number
    # call the recursive function, left_count,
    # which will store the length,
    # of the potenial range,
    # that occurs BEFORE the current number
        # pass the 0, as the current range length size
        # pass left, as the current number,
            # to start decrementing from
        # pass numbers, to identify if,
            # the number occurs in the input array
    
    right_count = count_right(0, right, numbers)
    # to explore the potential range that occurs,
    # AFTER the current number
    # call the recursive function, right_count,
    # which will store the length,
    # of the potenial range,
    # that occurs AFTER the current number
        # pass the 0, as the current range length size
        # pass right, as the current number,
            # to start incrementing from
        # pass numbers, to identify if,
            # the number occurs in the input array
    
    range_length += left_count
    range_length += right_count
    # increment the current number's range range_length,
    # by the left_count and right_count
    # now, we have the final count of the range,
    # that the current number contributes to
    
    
    if range_length > largest_range:
    # once we have finshed counting,
    # the current numbers range length,
    # then we need to check if,
    # the current numbers range length,
    # is the new longest range
        

        # if so, we want to update the varaibles,
        # that are related to the longest_range

        largest_range = range_length
        # update largest_range, so future iterations 
        # can compare thier range_length,
        # against the current largest range_length
        
        start = num - left_count
        # update start to equal the current num - left_count
            # start will now store the,
            # largest range_length starting number
        
        end = num + right_count
        # update start to equal the current end + right_count
            # start will now store the,
            # largest range_length ending number

        # if not, do nothing
        # if a range length is not longer than our largest range length,
        # we do not care about it,
        # and there is no action to take
        
    add_numbers(idx + 1, array, numbers)
    # call the recursive function, count_range_length,
    # which is the recursive call that will create a loop
    #
    # for each iteration of the recursive function, 
    # we need to increment the index,
    # so we can perform the same function,
    # on a different index in the array
    # and eventually reach our base case
    #
    # all other global running variables,
    # would have been updated already,
    # so just pass them as is

    return [start, end]
    # we need to return the start and end
    # to the largest_range_array variable in our main funciton
    # we can do this by simply returning those values,
    # at each recursive function instance



def count_left(left_count, left, numbers):
# the parameters for this recursive function are, 
# left_count: 
    # the current count of the range,
    # prior to the current number, 
    # incremented each recursive function call
    #
    # each recursive function call, 
    # has the opporunity to update left_count,
    # which is a "global" variable, 
    # that will be passed to the next,
    # recursive function call
        # regardless of an update or not
        # this will a running variable 
# left:
    # the next number to check if,
    # it is included in the input array
    # decremented each recursive function call
# numbers:
    #  the dictionary that stores all the numbers,
    #  all the numbers from the input array, 
    #  and, will allow us to check if,
    #  the current idx and corresponding number's,
    #  potenial range has been explored/counted
    
    if left not in numbers:
        return left_count
    # each recursive function call, 
    # will check,
    # if the base case has been acheived
        # the base case is to determine if left,
        # exists in the input array
        # if NOT, return the current left_count, 
        # at the time of this recursive function call,
        # back up the stack
        # 
        # if so, we have have found an 
        # additon number that contributes to,
        # the current number's range 
    
    numbers[left] = False
    # since we have found an addition number,
    # that contributes to the current number's range,
    # we should update the number's dictionary to,
    # reflect that left's range_length,
    # is being explored and does not need to be recounted.

    left_count = count_left(left_count + 1, left - 1, numbers)
    # call the recursive function, count_left,
    # which is the recursive call that will create a loop
    #
    # for each iteration of the recursive function, 
    # we need to decrement the left,
    # so we can perform the same function,
    # on a different number
    # and eventually reach our base case
    #
    # we also need to increment, left_count
    # because we found an addition number,
    # that contributes to the current number's range

    return left_count
    # after the base case is acheieved, 
    # the left_count of that recursive function 
    # will be returned up the stack 
    # and we need that version of left_count
    # to be returned to left_count
    # in the count_range_length function



def count_right(right_count, right, numbers):
# the parameters for this recursive function are, 
# right_count: 
    # the current count of the range,
    # AFTER to the current number, 
    # incremented each recursive function call
    #
    # each recursive function call, 
    # has the opporunity to update right_count,
    # which is a "global" variable, 
    # that will be passed to the next,
    # recursive function call
        # regardless of an update or not
        # this will a running variable 
# right:
    # the next number to check if,
    # it is included in the input array
    # incremented each recursive function call
# numbers:
    #  the dictionary that stores all the numbers,
    #  all the numbers from the input array, 
    #  and, will allow us to check if,
    #  the current idx and corresponding number's,
    #  potenial range has been explored/counted
    
    if right not in numbers:
        return right_count
    # each recursive function call, 
    # will check,
    # if the base case has been acheived
        # the base case is to determine if right,
        # exists in the input array
        # if NOT, return the current right_count, 
        # at the time of this recursive function call,
        # back up the stack
        # 
        # if so, we have have found an 
        # additon number that contributes to,
        # the current number's range 
    
    numbers[left] = False
    # since we have found an addition number,
    # that contributes to the current number's range,
    # we should update the number's dictionary to,
    # reflect that left's range_length,
    # is being explored and does not need to be recounted.

    right_count = count_right(right_count + 1, right + 1, numbers)
    # call the recursive function, count_right,
    # which is the recursive call that will create a loop
    #
    # for each iteration of the recursive function, 
    # we need to increment right,
    # so we can perform the same function,
    # on a the next greater number
    # and eventually reach our base case
    #
    # we also need to increment, right_count
    # because we found an addition number,
    # that contributes to the current number's range

    return right_count
    # after the base case is acheieved, 
    # the right_count of that recursive function 
    # will be returned up the stack 
    # and we need that version of right_count
    # to returned to right_count,
    # in the count_range_length function
'''

# Time: O(n) | # Space: O(n)
def largestRange_recursion(array):
    numbers = {}
    start = array[0]
    end = array[0]
    largest_range_array = [start, end]

    add_numbers(0, array, numbers)
    largest_range_array = count_range_length(0, 0, start, end, array, numbers)

    return largest_range_array

def add_numbers(idx, array, numbers):
    if idx >= len(array):
        return

    num = array[idx]
    numbers[num] = True

    add_numbers(idx + 1, array, numbers)

def count_range_length(idx, largest_range, start, end, array, numbers):
    if idx >= len(array):
        return [start, end]

    num = array[idx]

    if numbers[num] is True:
        numbers[num] = False

        range_length = 1
        left = num - 1
        right = num + 1

        left_count = count_left(0, left, numbers)
        right_count = count_right(0, right, numbers)

        range_length += left_count
        range_length += right_count

        if range_length > largest_range:
            largest_range = range_length
            start = num - left_count
            end = num + right_count

    count_range_length(idx + 1, largest_range, start, end, array, numbers)

    return [start, end]

def count_left(left_count, left, numbers):
    if left not in numbers:
        return left_count
    numbers[left] = False
    left_count = count_left(left_count + 1, left - 1, numbers)
    return left_count

def count_right(right_count, right, numbers):
    if right not in numbers:
        return right_count
    numbers[right] = False
    right_count = count_right(right_count + 1, right + 1, numbers)
    return right_count


array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print("array:", array)
print("largest_range:", largest_range(array))
print("largestRange_n:", largestRange_n(array))
print("largestRange:", largestRange(array))
print("largestRange_recursion:", largestRange_recursion(array))
print(" ")

array = [0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
print("array:", array)
print("largest_range:", largest_range(array))
print("largestRange_n:", largestRange_n(array))
print("largestRange:", largestRange(array))
print("largestRange_recursion:", largestRange_recursion(array))
print(" ")

array = [-1, 0, 1]
print("array:", array)
print("largest_range:", largest_range(array))
print("largestRange_n:", largestRange_n(array))
print("largestRange:", largestRange(array))
print("largestRange_recursion:", largestRange_recursion(array))
print(" ")