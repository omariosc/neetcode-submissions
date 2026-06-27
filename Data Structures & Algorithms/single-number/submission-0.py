class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = 0
        for n in nums:
            check ^= n
        return check