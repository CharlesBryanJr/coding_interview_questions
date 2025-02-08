# pylint: skip-file

'''

'''

from typing import List
from typing import Tuple
from collections import deque

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return 1


if __name__ == "__main__":
    senate = "DDRRR"
    print(f'senate: {senate}')
    solution = Solution()
    OUTPUT = solution.predictPartyVictory(senate)
    print(f'predictPartyVictory: {OUTPUT}')
    EXPECTED_OUTPUT = "Dire"
    print(f'Expected Output: {EXPECTED_OUTPUT}')
    print(f'OUTPUT == EXPECTED_OUTPUT: {OUTPUT == EXPECTED_OUTPUT}')