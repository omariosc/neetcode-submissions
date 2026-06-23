class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)

        hs = set(nums)
        longest = 1
        for i in hs:
            if i - 1 not in hs:
                j, candidate = i + 1, 1
                while j in hs:
                    j += 1
                    candidate += 1
                longest = max(longest, candidate)
        return longest