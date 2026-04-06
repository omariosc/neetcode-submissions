class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if abs(target) > total:
            return 0
        
        rows = len(nums) + 1
        cols = 2 * total + 1
        offset = total
        
        dp = [[0] * cols for _ in range(rows)]
        dp[0][offset] = 1  # 1 way to make sum 0 with no numbers
        
        for i in range(len(nums)):
            for s in range(-total, total + 1):
                ways = dp[i][s + offset]
                if ways > 0:
                    dp[i + 1][s + nums[i] + offset] += ways
                    dp[i + 1][s - nums[i] + offset] += ways
        
        return dp[len(nums)][target + offset]