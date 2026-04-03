class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_length = 0
        
        for i in nums:
            if int(i-1) not in nums:
                j, length = i+1, 1
                while j in nums:
                    length += 1
                    j += 1
                if length > max_length:
                    max_length = length

        return max_length
