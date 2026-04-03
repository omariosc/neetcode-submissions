class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def generatePermutations(i: int) -> List[List[int]]:
            if i == len(nums):
                return [[]]

            res = []
            perms = generatePermutations(i + 1)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res
            
        return generatePermutations(0)