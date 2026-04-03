class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lists = [[]]
        for i in nums:
            for l in lists[:]:
                new = l + [i]
                lists.append(new)
        return lists