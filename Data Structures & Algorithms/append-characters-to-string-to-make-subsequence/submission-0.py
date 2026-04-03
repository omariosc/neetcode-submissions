class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        iS = iT = 0
        while iS < len(s) and iT < len(t):
            if s[iS] == t[iT]:
                iT += 1
            iS += 1
        return len(t) - iT