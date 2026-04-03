class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum = 0.5*len(nums)*(len(nums)+1)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        return 0 if maximum == total else int(maximum - total)
            