class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(m-2, -1, -1):
            cp = [1] * n
            for c in range(n-2, -1, -1):
                cp[c] = dp[c] + cp[c+1]
            dp = cp
        return dp[0]