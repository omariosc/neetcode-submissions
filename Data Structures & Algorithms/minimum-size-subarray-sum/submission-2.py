class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("infinity")

        currSum = 0
        L = 0
        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                minLength = min(minLength, R - L + 1)
                currSum -= nums[L]
                L += 1

        return minLength if minLength != float("infinity") else 0