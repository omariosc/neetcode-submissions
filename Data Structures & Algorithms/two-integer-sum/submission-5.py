class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            n = nums[i]
            d = target - n
            try:
                j = table[str(d)]
                return [min(i,j),max(i,j)]
            except KeyError:
                table[str(n)] = i