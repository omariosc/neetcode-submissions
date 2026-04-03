from functools import reduce
from operator import ixor

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return reduce(lambda acc, i: acc ^ i ^ nums[i], range(len(nums)), len(nums))