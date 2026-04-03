class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums

        res = [[]]

        for n in nums:
            perms = []
            for p in res:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, n)
                    perms.append(pCopy)
            res = perms.copy()
            
        return res