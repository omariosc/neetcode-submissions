from functools import cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        @cache
        def dfs(i: int, c: int) -> int:
            if i == len(profit) or c <= 0:
                return 0

            skip = dfs(i + 1, c)
            
            take = 0
            if weight[i] <= c:
                take = profit[i] + dfs(i, c - weight[i])

            return max(skip, take)

        return dfs(0, capacity)