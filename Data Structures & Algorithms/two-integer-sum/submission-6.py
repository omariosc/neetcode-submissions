class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [min(i,j), max(i,j)]
        
