class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            row = words[i]
            col = ""
            for j in range(n):
                if i < len(words[j]):
                    col += words[j][i]
            
            if row != col:
                return False
        
        return True