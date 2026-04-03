class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n

        for i in range(n):
            xor ^= i
            xor ^= nums[i]

        return xor