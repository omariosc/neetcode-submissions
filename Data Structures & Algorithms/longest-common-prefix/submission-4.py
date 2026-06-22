class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length, shortest = len(strs[0]), strs[0]
        for s in strs:
            if len(s) < length:
                length, shortest = len(s), s
        
        for i in range(0, length):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i] if i != 0 else ""
        return shortest
                    

