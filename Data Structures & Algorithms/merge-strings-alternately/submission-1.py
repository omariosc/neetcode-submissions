class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        smaller = word1 if len(word1) < len(word2) else word2
        for i in range(len(smaller)):
            res.append(word1[i])
            res.append(word2[i])
        if smaller == word1:
            suffix = word2[len(word1):]
        else:
            suffix = word1[len(word2):]
        return "".join(res) + suffix
            
