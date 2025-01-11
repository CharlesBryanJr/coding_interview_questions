# pylint: skip-file

'''

'''

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros_count, max_length = 0, 0, 0
        for right, value in enumerate(nums):
            if value == 0:
                zeros_count += 1
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            max_length = max(max_length, right - left)
        return max_length


if __name__ == "__main__":
    nums = [0,1,1,1,0,1,1,0,1]
    print(f'nums: {nums}')
    solution = Solution()
    OUTPUT = solution.longestSubarray(nums)
    print(f'longestSubarray: {OUTPUT}')
    EXPECTED_OUTPUT = 5
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')