from functools import cache

class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n == 0: return 1
        if n == 1: return x
        
        extra = 1
        if n % 2 == 1: 
            extra = x
        
        half = self.myPow(x, n//2)
        return half * half * extra