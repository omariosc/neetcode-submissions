class Solution:
    def confusingNumber(self, n: int) -> bool:
        confused = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        start_number = str(n)
        final_number = ""
        original_n = n
        if n == 0: return False
        while n > 0:
            remainder = n % 10
            if remainder not in confused:
                return False
            final_number += str(confused[remainder])
            n = int(n // 10)
        if int(start_number) == int(final_number):
            return False
        return True