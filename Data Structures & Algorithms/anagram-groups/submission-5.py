from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            values = "".join(sorted(s))
            anagrams[values].append(s)
        
        return list(anagrams.values())