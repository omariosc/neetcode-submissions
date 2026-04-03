class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        elements = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                elements.remove(nums[L])
                L += 1
            if nums[R] in elements:
                return True
            else:
                elements.add(nums[R])
            
        return False