class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = []

        curr = max(a, b)
        carry = 0
        while curr > 0 or carry:
            bitA = a & 1
            bitB = b & 1
            
            total = 0
            if bitA == bitB and bitA:
                if carry:
                    total = 1
                carry = 1
            elif bitA != bitB and 1 == (bitA | bitB):
                if carry:
                    total = 0
                    carry = 1
                else:
                    total = 1
                    carry = 0
            elif carry:
                total = 1
                carry = 0

            result.append(total)

            a >>= 1
            b >>= 1
    
        return int("".join(result))