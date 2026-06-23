class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hs = set(nums)
        i = 1
        while i in hs:
            i += 1
        return i