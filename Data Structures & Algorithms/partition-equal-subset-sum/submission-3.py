class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        ROWS, COLS, target = len(nums) + 1, total + 1, total // 2
        dp = [[0] * COLS for _ in range(ROWS)]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if j >= nums[i-1]:
                    dp[i][j] = max(dp[i-1][j], nums[i-1] + dp[i-1][j-nums[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
                
                if dp[i][j] == target:
                    return True

        return False