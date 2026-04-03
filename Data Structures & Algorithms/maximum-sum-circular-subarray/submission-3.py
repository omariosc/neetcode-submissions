class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        # Standard Kadane's for max subarray (linear case)
        maxSum = nums[0]
        currMax = 0
        for x in nums:
            currMax = max(x, currMax + x)
            maxSum = max(maxSum, currMax)
            
        # Kadane's for min subarray to find max circular subarray
        minSum = nums[0]
        currMin = 0
        for x in nums:
            currMin = min(x, currMin + x)
            minSum = min(minSum, currMin)
            
        # If all numbers are negative, total_sum - minSum would be 0 (empty subarray)
        # In that case, return the linear maxSum
        if total_sum == minSum:
            return maxSum
            
        return max(maxSum, total_sum - minSum)