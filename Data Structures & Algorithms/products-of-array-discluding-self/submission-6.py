class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [], []
        tmpL, tmpR = 1, 1
        for i in range(len(nums)):
            tmpL *= nums[i]
            tmpR *= nums[len(nums) - i - 1]
            pre.append(tmpL)
            post.append(tmpR)
        post = post[::-1]

        res = []
        for i in range(len(nums)):
            before = pre[i - 1] if i > 0 else 1
            after = post[i + 1] if i < len(nums) - 1 else 1
            res.append(before * after)
        return res
        
        