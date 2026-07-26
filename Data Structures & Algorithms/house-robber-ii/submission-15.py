from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        @cache
        def helper(arr_tuple: tuple, i: int) -> int:
            if i >= len(arr_tuple):
                return 0
            take = arr_tuple[i] + helper(arr_tuple, i + 2)
            skip = helper(arr_tuple, i + 1)

            return max(take, skip)
        
        return max(helper(tuple(nums[:-1]), 0), helper(tuple(nums[1:]), 0))