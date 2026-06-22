class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0, 0, 0]
        for n in nums:
            freq[n] += 1
        
        i = 0
        for n in range(len(nums)):
            while freq[i] == 0:
                i += 1
            nums[n] = i
            freq[i] -= 1