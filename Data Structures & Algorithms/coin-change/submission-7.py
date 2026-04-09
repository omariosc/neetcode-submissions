from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        max_amount = amount + 1

        @cache
        def find(remain=amount):
            if remain < 0:
                return max_amount
            if remain == 0:
                return 0

            res = max_amount
            for c in coins:
                if c <= remain:
                    res = min(res, 1 + find(remain - c))
            return res

        ans = find()
        return ans if ans != max_amount else -1 