class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1
        dp = [0] * COLS        
        for i in range(ROWS):
            for j in range(COLS - 1, -1, -1):    
                if i == 0:
                    dp[j] = profit[0] if weight[0] <= j else 0
                    continue
                max_prev = dp[j-weight[i]] if j - weight[i] >= 0 else 0
                take = profit[i] + max_prev if j >= weight[i] else 0
                skip = dp[j]
                dp[j] = max(skip, take)
        return dp[COLS-1]