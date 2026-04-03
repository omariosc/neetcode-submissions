class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iS = iT = 0
        while iT < len(t) and iS < len(s):
            if s[iS] == t[iT]:
                iS += 1
            iT += 1
        if iS < len(s):
            return False
        return True