class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount

        for coin in coins:
            for target in range(1, amount + 1):
                if target - coin >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - coin])

        return dp[-1] if dp[-1] != float("inf") else -1