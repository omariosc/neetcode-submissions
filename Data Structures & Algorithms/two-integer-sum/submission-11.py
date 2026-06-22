class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i, n in enumerate(nums):
            if n in comps:
                return [comps[n], i]
            comps[target-n] = i