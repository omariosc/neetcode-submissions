class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:        
        counts = {}
        for s in strs:
            z = s.count("0")
            o = len(s) - z
            counts[s] = (z, o)
            
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs))]
        for i in range(len(strs)):
            cz, co = counts[strs[i]]
            for z in range(m + 1):
                for o in range(n + 1):
                    take = 0
                    if z-cz >= 0 and o-co >= 0:
                        if i > 0:
                            take += dp[i-1][z-cz][o-co]
                        take += 1

                    dp[i][z][o] = max(
                        dp[i-1][z][o] if i > 0 else 0,
                        take
                    )

        return dp[-1][-1][-1]
            
