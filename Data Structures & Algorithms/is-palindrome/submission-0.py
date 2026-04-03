class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = ""
        for c in s:
            if (c >= "0" and c <= "9") or (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
                parsed += c.lower()

        print(parsed)

        l = 0
        r = len(parsed) - 1

        while r > l:
            if parsed[l] != parsed[r]:
                return False
            l += 1
            r -= 1
        return True