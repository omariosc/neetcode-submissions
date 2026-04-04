class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
        if len(nums) == 1:
            return False

        L, R = 0, 1
        while L < len(nums):
            elements = set([nums[L]])
            while R - L <= k and R < len(nums):
                if nums[R] in elements:
                    return True
                elements.add(nums[R])
                R += 1
            elements.remove(nums[L])
            L += 1
        return False