from functools import cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1
        dp = [0] * COLS

        for i in range(ROWS):
            for j in range(1, COLS):
                take = profit[i] + dp[j - weight[i]] if j - weight[i] >= 0 else 0
                dp[j] = max(dp[j], take)
                
        return dp[-1]