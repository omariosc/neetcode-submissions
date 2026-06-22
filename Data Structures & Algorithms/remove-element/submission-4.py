class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        R = len(nums) - 1
        for L in range(0, len(nums)):
            while R >= 0 and nums[R] == val:
                R -= 1
            if L >= R:
                return L if nums[L] == val else L + 1
            if nums[L] == val:
                nums[L], nums[R] = nums[R], nums[L]


