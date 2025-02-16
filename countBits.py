# pylint: skip-file

'''

'''

from typing import List
from typing import Tuple
from collections import deque

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [1]


if __name__ == "__main__":
    n = 2
    print(f'n: {n}')
    solution = Solution()
    OUTPUT = solution.countBits(n)
    print(f'countBits: {countBits}')
    EXPECTED_OUTPUT = [0,1,1]
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')