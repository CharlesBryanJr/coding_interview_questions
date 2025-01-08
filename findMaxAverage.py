# pylint: skip-file

'''

'''


from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k


if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(f'nums: {nums}')
    print(f'k: {k}')
    solution = Solution()
    OUTPUT = solution.findMaxAverage(nums, k)
    print(f'findMaxAverage: {OUTPUT}')
    EXPECTED_OUTPUT = 12.75000
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')