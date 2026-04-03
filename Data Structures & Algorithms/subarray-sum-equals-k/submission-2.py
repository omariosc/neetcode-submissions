class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            if curSum - k in prefixSums:
                res += prefixSums[curSum - k]
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res