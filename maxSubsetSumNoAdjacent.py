'''maxSubsetSumNoAdjacent.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''

given:
- an array of postive integers

action:
-
return:
- the max sum of non-adjacent elements in the array.

note:
- if array length is 0, return 0


'''

# Time: O(n) | # Space: O(n)


def maxSubsetSumNoAdjacent_n(array):
    array_length = len(array)

    if array_length == 0:
        return 0
    if array_length == 1:
        return array[0]
    if array_length == 2:
        return max(array[0], array[1])

    running_sum_array = [array[0]]
    running_sum_array.append(max(array[0], array[1]))

    for idx in range(2, array_length):
        num = array[idx]

        last_num = running_sum_array[idx - 1]
        running_sum = running_sum_array[idx - 2] + num

        running_sum_array.append(max(last_num, running_sum))

    return running_sum_array[array_length - 1]


# Time: O(n) | # Space: O(1)
def maxSubsetSumNoAdjacent(array):
    array_length = len(array)

    if array_length == 0:
        return 0
    if array_length == 1:
        return array[0]
    if array_length == 2:
        return max(array[0], array[1])

    last_last = array[0]
    last = max(array[0], array[1])

    for idx in range(2, array_length):
        num = array[idx]
        running_sum = last_last + num

        last_last = last
        last = max(last, running_sum)

    return last


array = [75, 105, 120, 75, 90, 135]
print("array:", array)
print("maxSubsetSumNoAdjacent_n:", maxSubsetSumNoAdjacent_n(array))
print("maxSubsetSumNoAdjacent:", maxSubsetSumNoAdjacent(array))
print(" ")

array = [10, 5, 20, 25, 15, 5, 5, 15]
print("array:", array)
print("maxSubsetSumNoAdjacent_n:", maxSubsetSumNoAdjacent_n(array))
print("maxSubsetSumNoAdjacent:", maxSubsetSumNoAdjacent(array))
print(" ")

array = [7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4]
print("array:", array)
print("maxSubsetSumNoAdjacent_n:", maxSubsetSumNoAdjacent_n(array))
print("maxSubsetSumNoAdjacent:", maxSubsetSumNoAdjacent(array))
print(" ")

# _recursion
# _iteration
print(" ")
