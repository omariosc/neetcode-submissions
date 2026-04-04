class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = []
        totalSum = 0
        for n in nums:
            sums.append(totalSum)
            totalSum += n

        for i in range(len(nums)):
            leftSum = sums[i]
            rightSum = sums[i+1] if i + 1 < len(nums) else 0
            if leftSum == totalSum - rightSum:
                return i

        return -1