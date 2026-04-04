class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = sum(nums)
        
        prefix = []
        running = 0
        for n in nums:
            running += n
            prefix.append(running)
        
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if prefix[j] - prefix[i] + nums[i] == k:
                    res += 1
        
        return res