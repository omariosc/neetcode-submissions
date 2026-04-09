class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount

        for coin in coins:
            for target in range(1, amount + 1):
                skip = dp[target]
                take = float("inf")
                if target - coin >= 0:
                    take = 1 + dp[target - coin]

                dp[target] = min(skip, take)

        return dp[-1] if dp[-1] != float("inf") else -1