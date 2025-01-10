# pylint: skip-file

'''
'''

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end, n = 0, 1, len(nums)
        ones_length, max_ones_length = 0, -1
        filp_count = k

        while start < n and end < n:
            while start < n and nums[start] == 0:
                start += 1
            
            end = start + 1
            while end < n and nums[end] == 1:
                end += 1
            
            if start < n and end < n:
                print(f'start: {start}')
                print(f'nums[start]: {nums[start]}')
                print(f'end: {end}')
                print(f'nums[end]: {nums[end]}')

            while start > 0 and nums[start] == 0 and filp_count > 0:
                start -= 1
                filp_count -= 1
            start = max(start, 0)
            
            filp_count -= 1
            while end < n and nums[end] == 0 and filp_count > 0:
                end += 1
                filp_count -= 1
            
            if start < n and end < n:
                print(f'start: {start}')
                print(f'nums[start]: {nums[start]}')
                print(f'end: {end}')
                print(f'nums[end]: {nums[end]}')
            

            ones_length = end - start + 1
            if ones_length > max_ones_length:
                max_ones_length = ones_length
            print(f'ones_length: {ones_length}')
            print(f'max_ones_length: {max_ones_length}')
            print()

            start = end
            filp_count = k

        return max_ones_length


if __name__ == "__main__":
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(f'nums: {nums}')
    print(f'k: {k}')
    solution = Solution()
    OUTPUT = solution.longestOnes(nums, k)
    print(f'longestOnes: {OUTPUT}')
    EXPECTED_OUTPUT = 10
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')