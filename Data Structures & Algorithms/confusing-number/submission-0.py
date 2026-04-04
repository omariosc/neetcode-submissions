class Solution:
    def confusingNumber(self, n: int) -> bool:
        confused = [0, 1, 6, 8, 9]
        while n > 0:
            remainder = n % 10
            if remainder not in confused:
                return False
            n //= 10
        return True