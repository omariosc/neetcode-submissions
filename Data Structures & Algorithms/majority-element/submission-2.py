class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, count = nums[0], 0
        for n in nums:
            if n == maj:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj, count = n, 1
        return maj