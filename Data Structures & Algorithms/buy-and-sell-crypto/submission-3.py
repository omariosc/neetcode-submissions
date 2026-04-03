class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy = prices[0]
        sell = prices[-1]
        res = sell - buy

        for i in range(len(prices)):
            if prices[i] > sell:
                sell = prices[i]
                res = max(res, sell - buy)
            elif prices[i] < buy:
                buy = prices[i]
                sell = prices[i]

        return res
