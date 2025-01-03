# pylint: skip-file

'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        MIN_NUM = min(nums)    
        MAX_NUM = max(nums)
        print(f'MIN_NUM: {MIN_NUM}')
        print(f'MAX_NUM: {MAX_NUM}')
        for NUM_IDX in range(len(nums)):
            if nums[NUM_IDX] == MIN_NUM:
                MIN_NUM_IDX = NUM_IDX
            elif nums[NUM_IDX] == MAX_NUM:
                MAX_NUM_IDX = NUM_IDX
        if MAX_NUM_IDX - MIN_NUM_IDX > 0:
            return True
        i, j = 0, 1
        while nums[j] in (MIN_NUM, MAX_NUM):
            j += 1
        k = j + 1
        while nums[k] in (MIN_NUM, MAX_NUM):
            k += 1
        print(f'nums[i:{i}]: {nums[i]}')
        print(f'nums[j:{j}]: {nums[j]}')
        print(f'nums[k:{k}]: {nums[k]}')
        return False


if __name__ == "__main__":
    nums = [20,100,10,12,5,13]
    print(f'nums: {nums}')
    solution = Solution()
    OUTPUT = solution.increasingTriplet(nums)
    print(f'increasingTriplet: {OUTPUT}')
    EXPECTED_OUTPUT = True
    print(f'Expected Output: {OUTPUT == EXPECTED_OUTPUT}')