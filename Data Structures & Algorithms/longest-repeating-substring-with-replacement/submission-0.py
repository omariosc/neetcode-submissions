class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        maxLength = L = 0
        for c in s:
            counter[c] += 1
            while L < len(s) and self.computeRequiredReplacements(counter) > k:
                counter[s[L]] -= 1
                if counter[s[L]] == 0:
                    del counter[s[L]]
                L += 1
            maxLength = max(sum(counter.values()), maxLength)
        return maxLength

    def computeRequiredReplacements(self, counter: Dict[str,int]) -> int:
        counterLength = sum(counter.values())
        required_replacements = counterLength - max(counter.values())
        return required_replacements
