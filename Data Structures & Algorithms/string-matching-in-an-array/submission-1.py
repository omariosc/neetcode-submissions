class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words.sort()
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res