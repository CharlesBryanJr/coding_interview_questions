# pylint: skip-file

'''

'''

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        running_sum, largest_altitude = 0, 0
        for num in gain:
            running_sum += num
            if running_sum > largest_altitude:
                largest_altitude = running_sum
        return largest_altitude


if __name__ == "__main__":
    gain = [-5,1,5,0,-7]
    print(f'gain: {gain}')
    solution = Solution()
    OUTPUT = solution.largestAltitude(gain)
    print(f'largestAltitude: {OUTPUT}')
    EXPECTED_OUTPUT = 1
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')