class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        r = 0
        for word in words:
            consistent = True
            for c in word:
                if c not in allowed_set:
                    consistent = False
            if consistent: 
                r += 1
        return r