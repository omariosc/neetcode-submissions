class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        minLength = length + 1
        currSum = L = 0
        
        for R in range(0, length):
            currSum += nums[R]
            while currSum >= target:
                minLength = min(minLength, R - L + 1)
                currSum -= nums[L]
                L += 1

        return 0 if minLength == length + 1 else minLength