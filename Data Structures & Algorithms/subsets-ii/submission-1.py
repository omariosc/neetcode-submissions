class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curr = [], []
        Solution.produceSubsets(0, nums, curr, subsets)
        return subsets
    
    @staticmethod
    def produceSubsets(i: int, nums: List[int], curr: List[int], subsets: List[List[int]]) -> None:
        if i == len(nums):
            subsets.append(curr.copy())
            return

        curr.append(nums[i])
        Solution.produceSubsets(i+1, nums, curr, subsets)

        curr.pop()
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        Solution.produceSubsets(i+1, nums, curr, subsets)