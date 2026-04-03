class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        maxI = 0
        while i < len(nums):
            currI = 0
            while i < len(nums) and nums[i] == 1:
                currI += 1
                i += 1
            maxI = max(maxI, currI)
            i += 1
        return maxI