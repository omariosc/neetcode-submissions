from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dfs(i: int, total: int) -> None:
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0

            return dfs(i + 1, total) + dfs(i, total + coins[i])

        return dfs(0, 0)