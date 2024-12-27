'''three_number_sum.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
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

given:
- a non empty array of distinct integers
- an integer target sum

return:
- a two dimensional array of
- all triplets that sum to the given integer target sum

note:
- ascending order for numbers in each triplet
- ascending order for triplets themselves, with respect to the numbers they hold

targetSum = a + b + c
a = targetSum - b - c
b = targetSum - a - c
c = targetSum - a - b
'''

# Time: O(n^2) | # Space: O(n)
def threeNumberSum(array, targetSum):
    array.sort()
    three_number_sum = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            summation = array[i] + array[left] + array[right]
            if summation == targetSum:
                three_number_sum.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif summation < targetSum:
                left += 1
            elif summation > targetSum:
                right -= 1
    return three_number_sum

def three_number_sum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)):
        two_number_sum(i, triplets, array, targetSum)
    return triplets

def two_number_sum(i, triplets, array, targetSum):
    left = i + 1
    right = len(array) - 1
    while left < right:
        summation = array[i] + array[left] + array[right]
        if summation == targetSum:
            triplets.append([array[i], array[left], array[right]])
            left += 1
            right -= 1
        elif summation < targetSum:
            left += 1
        elif summation > targetSum:
            right -= 1
    return triplets


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print("array:", array)
print("targetSum:", targetSum)
print(threeNumberSum(array, targetSum))
print(three_number_sum(array, targetSum))
print(" ")

array = [1, 2, 3]
targetSum = 6
print("array:", array)
print("targetSum:", targetSum)
print(threeNumberSum(array, targetSum))
print(three_number_sum(array, targetSum))
print(" ")

array = [8, 10, -2, 49, 14]
targetSum = 57
print("array:", array)
print("targetSum:", targetSum)
print(threeNumberSum(array, targetSum))
print(three_number_sum(array, targetSum))
print(" ")


# _recursion
# _iteration