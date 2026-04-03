class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
        
        # zero = 0
        # product = 1
        # for n in nums:
        #     if n != 0:
        #         product *= n
        #     else:
        #         zero += 1
        # res = []
        # if zero >= 2:
        #     return [0 for n in nums]
        # for n in nums:
        #     if n != 0 and not zero:
        #         res.append(int(product/n))
        #     elif n != 0 and zero:
        #         res.append(0)
        #     else:
        #         res.append(product)
        # return res