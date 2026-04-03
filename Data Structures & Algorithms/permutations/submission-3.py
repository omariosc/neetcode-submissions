class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return Solution.helper(0, nums)
    
    @staticmethod
    def helper(idx: int, nums: List[int]) -> List[List[int]]:
        if idx == len(nums):
            return [[]]

        res = []
        perms = Solution.helper(idx + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[idx])
                res.append(pCopy)
        return res