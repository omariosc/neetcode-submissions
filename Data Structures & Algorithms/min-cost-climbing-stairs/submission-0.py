from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def takeStep(i: int) -> int:
            if i >= len(cost):
                return 0
            return cost[i] + min(takeStep(i+1), takeStep(i+2))
        return min(takeStep(0), takeStep(1))