def longestSubarrayWithSum(array, targetSum):
    longest_subarray = []
    longest_subarray_count = -1

    start = end = currentSum = 0

    while end < len(array):
        currentSum += array[end]

        while start < end and currentSum > targetSum:
            currentSum -= array[start]
            start += 1

        if currentSum == targetSum:
            currentRange = end - start
            if currentRange > longest_subarray_count:
                longest_subarray_count = currentRange
                longest_subarray = [start, end]

        end += 1

    return longest_subarray