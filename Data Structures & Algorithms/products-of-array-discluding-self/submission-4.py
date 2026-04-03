class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        product = 1
        for n in nums:
            if n != 0:
                product *= n
            else:
                zero += 1
        res = []
        if zero >= 2:
            return [0 for n in nums]
        for n in nums:
            if n != 0 and not zero:
                res.append(int(product/n))
            elif n != 0 and zero:
                res.append(0)
            else:
                res.append(product)
        return res