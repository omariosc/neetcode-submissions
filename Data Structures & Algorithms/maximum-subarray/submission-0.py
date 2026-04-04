class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            if currSum > 0:
                currSum += nums[i]
                maxsum = max(maxsum, currSum)
            else:
                currSum = nums[i]
        return maxsum