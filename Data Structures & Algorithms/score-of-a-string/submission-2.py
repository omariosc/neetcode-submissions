class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        values = {}
        for letter in "abcdefghijklmnopqrstuvwxyz":
            values[letter] = ord(letter)
        for i in range(len(s)-1):
            score += abs(values[s[i+1]] - values[s[i]])
        return score