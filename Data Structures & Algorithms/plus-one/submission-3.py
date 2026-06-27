class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1
        return digits if not carry else [1] + digits