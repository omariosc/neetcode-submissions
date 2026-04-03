class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        values = {}
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            values[letter] = ord(letter)
        if len(s) == 1:
            return 0
        for i in range(len(s)-1):
            score += abs(values[s[i+1]] - values[s[i]])
        return score