class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2 + 1

        memo = {}
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(2*total - stoneSum)
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = min(
                dfs(i + 1, total),
                dfs(i + 1, total + stones[i])
            )
            return memo[(i, total)]
        
        return dfs(0, 0)