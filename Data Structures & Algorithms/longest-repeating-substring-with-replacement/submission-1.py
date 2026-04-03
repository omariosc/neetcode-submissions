class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        maxFreq = maxLength = L = 0
        
        for R in range(len(s)):
            counter[s[R]] += 1
            maxFreq = max(maxFreq, counter[s[R]])
            while R - L + 1 - maxFreq > k:
                counter[s[L]] -= 1
                L += 1
            maxLength = max(R - L + 1, maxLength)
        return maxLength