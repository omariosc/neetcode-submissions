class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for n in nums:
            if seen & (1 << n):
                return n
            seen |= (1 << n)