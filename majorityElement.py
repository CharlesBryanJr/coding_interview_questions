'''majorityElement'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=E0401
print(" ")

'''

Type of Question:
- array question

Clarifying Questions / Insights:
- input is an array of postive integers
- a single majority element does exist
- majority = len(array) // 2

Edge cases:
-

Base case:
-

Question:
- find the majority element from an array

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Min/Max Int

		- Tuples
			- Named elements
		- Arrays
			- Empty array
			- Nested or not nested
		- Dictionaries (Hashmaps)
			- Collisions

- If I knew / had this....
	-

Output:
-
'''

# Time: O(n) | # Space: O(n)
def majorityElement_n_n(array):
    majority = len(array) / 2
    nums = {}
    for num in array:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1

    most_common_element_count = max(nums.values())
    if most_common_element_count < majority:
        return -1

    for num in array:
        if nums[num] == most_common_element_count:
            return num
    return -1


# Time: O(nlog(n)) | # Space: O(1)
def majorityElement_nlogn_1(array):
    array.sort()
    return array[len(array) // 2]


# Time: O(n) | # Space: O(1)
def majorityElement_iteration(array):
    majority_element = None
    majority_element_count = 0

    for num in array:
        if majority_element_count == 0:
            majority_element = num

        if num == majority_element:
            majority_element_count += 1
        else:
            majority_element_count -= 1

    return majority_element


# Time: O(n) | # Space: O(1)
def majorityElement_recursion(array):
    return majority_element_recursion(0, array, 0, None)


def majority_element_recursion(i, array, count, answer):
    if i >= len(array):
        return answer

    if count == 0:
        answer = array[i]

    if array[i] == answer:
        count += 1
    else:
        count -= 1

    return majority_element_recursion(i + 1, array, count, answer)


array = [1, 2, 1]
print("array:", array)
print("majorityElement_n_n:", majorityElement_n_n(array))
array = [1, 2, 1]
print("majorityElement_nlogn_1:", majorityElement_nlogn_1(array))
array = [1, 2, 1]
print("majorityElement_iteration:", majorityElement_iteration(array))
array = [1, 2, 1]
print("majorityElement_recursion:", majorityElement_recursion(array))
print(" ")

array = [1, 2, 3, 2, 2, 1, 2]
print("array:", array)
print("majorityElement_n_n:", majorityElement_n_n(array))
array = [1, 2, 3, 2, 2, 1, 2]
print("majorityElement_nlogn_1:", majorityElement_nlogn_1(array))
array = [1, 2, 3, 2, 2, 1, 2]
print("majorityElement_iteration:", majorityElement_iteration(array))
array = [1, 2, 3, 2, 2, 1, 2]
print("majorityElement_recursion:", majorityElement_recursion(array))
print(" ")

array = [435, 6543, 6543, 435, 535, 6543, 6543, 12, 43, 6543, 6543]
print("array:", array)
print("majorityElement_n_n:", majorityElement_n_n(array))
array = [435, 6543, 6543, 435, 535, 6543, 6543, 12, 43, 6543, 6543]
print("majorityElement_nlogn_1:", majorityElement_nlogn_1(array))
array = [435, 6543, 6543, 435, 535, 6543, 6543, 12, 43, 6543, 6543]
print("majorityElement_iteration:", majorityElement_iteration(array))
array = [435, 6543, 6543, 435, 535, 6543, 6543, 12, 43, 6543, 6543]
print("majorityElement_recursion:", majorityElement_recursion(array))
print(" ")
