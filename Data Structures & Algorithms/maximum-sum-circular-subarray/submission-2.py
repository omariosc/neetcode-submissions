class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        cutOff, stopped = -1, False

        L = 0
        for R in range(len(nums)):
            if currSum + nums[R] < 0:
                currSum = 0
                L = R
                stopped = True
            else:
                currSum += nums[R]
            if currSum > maxSum:
                maxSum = currSum
                cutOff = R-1

        if not stopped:
            return maxSum

        for i in range(cutOff):
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum

        return maxSum
