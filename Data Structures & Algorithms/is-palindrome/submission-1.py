class Solution:

    def isValidChar(self, c: str) -> bool:
        return (c >= "0" and c <= "9") or (c >= "a" and c <= "z") or (c >= "A" and c <= "Z")

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while r > l:
            while not self.isValidChar(s[l]) and l < r:
                l += 1
            while not self.isValidChar(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True