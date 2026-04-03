class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.sidekick(nums, len(nums)-1, {})
        
    def sidekick(self, nums: List[int], n: int, memo: dict[int,int]) -> int:
        if n == 0:
            return nums[0]
        elif n == 1:
            return max(nums[0], nums[1])
        
        if n not in memo:
            memo[n] = max(self.sidekick(nums, n-1, memo), self.sidekick(nums, n-2, memo) + nums[n])
        
        return memo[n]

        

        