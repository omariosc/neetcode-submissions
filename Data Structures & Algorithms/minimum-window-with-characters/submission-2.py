class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        seen = {c: 0 for c in counter.keys()}
        total, currTotal = len(counter.keys()), 0
        found = (float("inf"), 0, len(s))

        L = 0
        for R, c in enumerate(s):
            if c in counter:
                seen[c] += 1
                if seen[c] == counter[c]:
                    currTotal += 1
            while L <= R and currTotal == total:
                if R - L + 1 < found[0]:
                    found = (R - L + 1, L, R)
                if s[L] not in counter:
                    L += 1
                    continue
                if seen[s[L]] == counter[s[L]]:
                    currTotal -= 1
                seen[s[L]] -= 1
                L += 1

        return s[found[1]:found[2]+1] if found[0] != float("inf") else ""