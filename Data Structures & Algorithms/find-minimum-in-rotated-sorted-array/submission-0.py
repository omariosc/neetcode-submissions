class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # If the array is not rotated at all
        if nums[0] < nums[-1]:
            return nums[0]

        return nums[self.binary_search(nums, 0, len(nums) - 1)]

    def binary_search(self, nums, l, r) -> int:
        while l <= r:
            mid = l + (r-l)//2    
            # Check if mid is the inflection point
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                return mid + 1
            # Decide which half to search
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        return 0