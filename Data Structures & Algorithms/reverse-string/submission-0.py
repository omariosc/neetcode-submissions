class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) % 2 == 0:
            l = (len(s) // 2) - 1
            r = l + 1
        else:
            l = (len(s) // 2) - 1
            r = l + 2
        while l >= 0 and r < len(s):
            s[l], s[r] = s[r], s[l]
            l -= 1
            r += 1
        return s
