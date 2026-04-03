class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indices = {}
        for i, c in enumerate(keyboard):
            indices[c] = i
        
        total = 0
        previous = 0
        for c in word:
            total += abs(previous - indices[c])
            previous = indices[c]
        return total
