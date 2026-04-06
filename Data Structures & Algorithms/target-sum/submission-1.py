class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(i: int, t: int) -> int:
            if (i,t) in memo:
                return memo[(i,t)]
            if i == len(nums):
                return 1 if t == 0 else 0

            subtract = dfs(i+1, t - nums[i])
            add = dfs(i+1, t + nums[i])
            memo[(i,t)] = subtract + add
            return memo[(i,t)]
        
        return dfs(0, target)
            
            