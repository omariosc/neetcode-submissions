from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            values = "".join(sorted(s))
            anagrams[values].append(s)
        
        res = []
        for anagram, words in anagrams.items():
            tmp = []
            for word in words:
                tmp.append(word)
            res.append(tmp)
        return res