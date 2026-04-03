class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, target, 0, len(nums) - 1)

    def _search(self, nums, target, l, r):
        if l > r:
            return -1

        mid = l + (r - l) // 2

        if nums[mid] < target:
            return self._search(nums, target, mid + 1, r)
        elif nums[mid] > target:
            return self._search(nums, target, l, mid - 1)
        else:
            return mid