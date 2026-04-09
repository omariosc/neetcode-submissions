from bisect import bisect_left

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days) + 1
        dp = [0] * n
        for i in range(1, n):
            idx7 = bisect_left(days, days[i-1] - 6)
            idx30 = bisect_left(days, days[i-1] - 29)
            
            dp[i] = min(
                costs[0] + dp[i-1],
                costs[1] + dp[idx7],
                costs[2] + dp[idx30]
            )
        
        return dp[-1]