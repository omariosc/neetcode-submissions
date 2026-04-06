class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        ROWS, COLS = len(nums), total // 2 + 1
        dp = [0] * COLS        
        for i in range(ROWS):
            for j in range(COLS - 1, 0, -1):
                max_prev = dp[j-nums[i]] if j - nums[i] >= 0 else 0
                take = nums[i] + max_prev if j >= nums[i] and nums[i] + max_prev <= j else 0
                skip = dp[j]
                dp[j] = max(skip, take)
        return dp[COLS-1] == COLS - 1