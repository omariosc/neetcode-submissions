class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = minSum = nums[0]
        total_sum = currMax = currMin = 0
        for x in nums:
            currMax = max(x, currMax + x)
            maxSum = max(maxSum, currMax)
            currMin = min(x, currMin + x)
            minSum = min(minSum, currMin)
            total_sum += x

        if total_sum == minSum:
            return maxSum
            
        return max(maxSum, total_sum - minSum)