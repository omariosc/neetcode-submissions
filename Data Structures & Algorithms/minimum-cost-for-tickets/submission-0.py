from functools import cache
from bisect import bisect_left

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(days):
                return 0

            j = bisect_left(days, days[i] + 7)
            k = bisect_left(days, days[i] + 30)
            return min(
                costs[0] + dfs(i + 1),
                costs[1] + dfs(j),
                costs[2] + dfs(k)
            )
        return dfs(0)