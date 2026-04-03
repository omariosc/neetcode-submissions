class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bit = 1 << len(nums)
        for n in nums:
            before = bit
            bit ^= 1 << n
            if bit < before:
                return n