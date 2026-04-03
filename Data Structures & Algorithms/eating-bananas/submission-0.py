import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l) // 2
            if self.timeToEat(piles, mid) <= h:
                r = mid
            else:
                l = mid + 1

        return l

    def timeToEat(self, piles: List[int], k: int) -> int:
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours