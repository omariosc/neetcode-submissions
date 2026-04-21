class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # Find the pivot (index of the maximum element)
        pivot = self.pivot_search(nums, 0, len(nums) - 1)

        # Decide which half to search
        if target >= nums[0] and target <= nums[pivot]:
            return self.binary_search(nums, 0, pivot, target)
        else:
            return self.binary_search(nums, pivot + 1, len(nums) - 1, target)
        
    def pivot_search(self, nums: List[int], l: int, r: int) -> int:
        # If array is not rotated, the last element is the max
        if nums[l] <= nums[r]:
            return r
        while l <= r:
            m = l + (r - l) // 2
            if m + 1 < len(nums) and nums[m] > nums[m+1]:
                return m
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return 0
    
    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1