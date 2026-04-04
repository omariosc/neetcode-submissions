class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = False
        product = 1
        for n in nums:
            if n != 0:
                product *= n
            else:
                zero = True
        res = []
        for n in nums:
            if n != 0 and not zero:
                res.append(int(product/n))
            elif (n != 0 and zero) or (n == 0 and zero):
                res.append(0)
            else:
                res.append(product)
        return res