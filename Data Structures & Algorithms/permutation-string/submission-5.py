from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        counter = Counter(s1)
        l = 0

        for r in range(n):
            counter[s2[r]] -= 1

            if r - l + 1 > m:
                counter[s2[l]] += 1
                l += 1

            if r - l + 1 == m and all(v == 0 for v in counter.values()):
                return True

        return False