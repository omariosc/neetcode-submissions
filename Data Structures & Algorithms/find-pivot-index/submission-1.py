class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = []
        totalSum = 0
        for n in nums:
            sums.append(totalSum)
            totalSum += n

        for i in range(len(nums)):
            leftSum = sums[i]
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i

        return -1