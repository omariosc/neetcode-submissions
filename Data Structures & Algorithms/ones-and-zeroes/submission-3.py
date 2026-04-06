from functools import cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:        
        counts = {s: (s.count("0"), s.count("1")) for s in strs}

        @cache
        def dfs(i: int, zeroes: int, ones: int):
            if zeroes < 0 or ones < 0:
                return 0
            if i == len(strs):
                return 0

            skip = dfs(i + 1, zeroes, ones)
            zero_count, one_count = counts[strs[i]]
            if zeroes >= zero_count and ones >= one_count:
                take = 1 + dfs(i + 1, zeroes - zero_count, ones - one_count)
            else:
                take = 0

            return max(skip, take)
        
        return dfs(0, m, n)

            
