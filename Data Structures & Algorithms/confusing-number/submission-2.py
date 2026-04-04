class Solution:
    def confusingNumber(self, n: int) -> bool:
        confused = {0: 0, 1: 1, 6: 9, 8: 8, 9: 9}
        start_number = str(n)
        final_number = ""
        while n > 1:
            remainder = n % 10
            if remainder not in confused:
                return False
            final_number += str(confused[remainder])
            n = int(n // 10)
        if start_number == final_number:
            return False
        return True