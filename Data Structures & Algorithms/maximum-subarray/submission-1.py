class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-infinity")
        currSum = float("-infinity")
        for i in range(0, len(nums)):
            if currSum > 0:
                currSum += nums[i]
            else:
                currSum = nums[i]
            maxsum = max(maxsum, currSum)
        return maxsum