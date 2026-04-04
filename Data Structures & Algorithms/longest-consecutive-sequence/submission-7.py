class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        nums = sorted(list(set(nums)), reverse=False)
        
        l = 1
        r = 1
        m = 1

        print(nums)
        while r != len(nums):
            if nums[r] == nums[r-1] + 1:
                l += 1
                if l > m:
                    m = l
            else:
                l = 0
            r += 1

        return m