class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        memo = {}
        def dfs(idx: int, currCap: int) -> int:
            if idx == len(profit):
                return 0
            if (idx, currCap) in memo:
                return memo[(idx, currCap)]
            
            maxProfit = dfs(idx + 1, currCap)

            newCap = currCap - weight[idx]
            if newCap >= 0:
                p = profit[idx] + dfs(idx + 1, newCap)
                maxProfit = max(p, maxProfit)
            
            memo[(idx, currCap)] = maxProfit
            return maxProfit
        
        return dfs(0, capacity)