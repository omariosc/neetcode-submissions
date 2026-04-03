from collections import Counter
from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        uniques = (x for x, cnt in c.items() if cnt == 1)
        return max(uniques, default=-1)