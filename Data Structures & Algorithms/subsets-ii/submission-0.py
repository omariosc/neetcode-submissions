class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lists = [[]]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                new_subsets = [l + [nums[i]] for l in last_added]
            else:
                new_subsets = [l + [nums[i]] for l in lists]
            last_added = new_subsets
            lists.extend(new_subsets)
        return lists