class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]

        for n in nums:
            colors[n] += 1
        
        i = 0
        for c in range(len(colors)):
            for _ in range(colors[c]):
                nums[i] = c
                i += 1     
        