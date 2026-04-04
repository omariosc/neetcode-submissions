class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = False
        product = 1
        for n in nums:
            if n != 0:
                product *= n
        res = []
        for n in nums:
            if n != 0:
                res.append(int(product/n))
            else:
                res.append(product)
        return res