'''kadanes_algorithm.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- non empty array of integers

action:
-

return:
- maximum subarray sum contained within the given array

note:
- subarray == contain only adjacent numbers


'''

# Time: O(n) | # Space: O(n)
def kadanesAlgorithm_n(array):
    kadanes = array[0]
    kadanes_array = [kadanes]

    for idx in range(1, len(array)):
        last_num = kadanes_array[idx - 1]
        num = array[idx]

        kadanes = max(num, last_num + num)
        kadanes_array.append(kadanes)

    return max(kadanes_array)

# Time: O(n) | # Space: O(1)
def kadanesAlgorithm(array):
    max_sum_at_idx = array[0]
    max_sum = array[0]

    for idx in range(1, len(array)):
        num = array[idx]
        max_sum_at_idx += num

        max_sum_at_idx = max(num, max_sum_at_idx)
        max_sum = max(max_sum, max_sum_at_idx)

    return max_sum

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print("array:", array)
print("kadanesAlgorithm_n:", kadanesAlgorithm_n(array))
print("kadanesAlgorithm:", kadanesAlgorithm(array))
print(" ")

array = [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]
print("array:", array)
print("kadanesAlgorithm_n:", kadanesAlgorithm_n(array))
print("kadanesAlgorithm:", kadanesAlgorithm(array))
print(" ")

array = [3, 4, -6, 7, 8, -15, 100]
print("array:", array)
print("kadanesAlgorithm_n:", kadanesAlgorithm_n(array))
print("kadanesAlgorithm:", kadanesAlgorithm(array))
print(" ")

# _recursion
# _iteration
print(" ")