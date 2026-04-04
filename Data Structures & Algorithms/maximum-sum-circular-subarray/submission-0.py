class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        cutOff = -1

        L = 0
        for R in range(len(nums)):
            if currSum + nums[R] < 0:
                currSum = 0
                L = R
            else:
                currSum += nums[R]
            if currSum > maxSum:
                maxSum = currSum
                cutOff = R-1

        for i in range(cutOff):
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum

        return maxSum
