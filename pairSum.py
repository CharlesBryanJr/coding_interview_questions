# pylint: skip-file

'''

'''

from typing import List
from typing import Tuple
from collections import deque

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        return 1


if __name__ == "__main__":
    head = [5,4,2,1]
    print(f'head: {head}')
    solution = Solution()
    OUTPUT = solution.pairSum(head)
    print(f'pairSum: {OUTPUT}')
    EXPECTED_OUTPUT = "Dire"
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')