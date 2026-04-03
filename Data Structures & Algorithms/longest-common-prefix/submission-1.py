class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        if not strs:
            return prefix

        for i in range(len(strs[0])):
            c = strs[0][i]
            common = True
            for s in range(len(strs)):
                if i >= len(strs[s]) or strs[s][i] != c:
                    common = False
                    break
            if common: 
                prefix += c        
            else:
                break

        return prefix
