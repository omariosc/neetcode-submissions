class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.s = s
        
        def producePartitions(curr: List[str], i: int):
            if i == len(s):
                self.res.append(curr.copy())
                return
            
            for end in range(i + 1, len(s) + 1):
                substring = self.s[i:end]
                if substring == substring[::-1]:
                    curr.append(substring)
                    producePartitions(curr, end)
                    curr.pop()
                

        producePartitions([], 0)
        return self.res