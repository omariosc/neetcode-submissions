from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ROWS = len(coins) + 1
        COLS = amount + 1
        dp = [[0] * COLS for _ in range(ROWS)]
        for i in range(ROWS):
            dp[i][0] = 1

        for i in range(1, ROWS):
            cur = coins[i-1]
            for j in range(COLS):
                dp[i][j] = dp[i-1][j]
                if j >= cur:
                    dp[i][j] += dp[i][j - cur]

        return dp[-1][-1]

        @cache
        def dfs(i: int, total: int) -> None:
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0

            return dfs(i + 1, total) + dfs(i, total + coins[i])

        return dfs(0, 0)