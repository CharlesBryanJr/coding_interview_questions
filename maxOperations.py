# pylint: skip-file
'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 
Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operation_count = 0
        used_nums_idx = [False] * len(nums)
        pairs = {}
        i = 0
        for i in range(len(nums)):
            print(f'i: {i}')
            if nums[i] in pairs:
                pairs[nums[i]] += [i]
            else:
                pairs[nums[i]] = [i]
            diff = k - nums[i]
            if diff in pairs:
                diff_idx = pairs[diff][0]
                print(f'FOUND PAIR')
                print(f'i: {i} with value: {nums[i]}')
                print(f'i: {diff_idx} with value: {diff}')
                print(f'pairs[{diff}]: {pairs[diff]}')
                pairs[diff].pop(0)
                if not pairs[diff]:
                    del pairs[diff]
                    print(f'del pairs[{diff}]')
                print(f'{pairs}')
                used_nums_idx[i] = True
                used_nums_idx[diff_idx] = True
                operation_count += 1
                print(f'operation_count: {operation_count}')
                print(f'used_nums_idx: {used_nums_idx}')
            print(f'{pairs}')
            print()
        return 0


if __name__ == "__main__":
    nums = [1,2,3,4]
    k = 5
    print(f'nums: {nums}')
    print(f'k: {k}')
    solution = Solution()
    OUTPUT = solution.maxOperations(nums, k)
    print(f'maxOperations: {OUTPUT}')
    EXPECTED_OUTPUT = 2
    print(f'Expected Output: {OUTPUT == EXPECTED_OUTPUT}')