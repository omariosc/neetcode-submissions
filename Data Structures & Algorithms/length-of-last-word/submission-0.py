class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1

        space = False
        c = 0

        for i in range(len(s)-1, 0, -1):
            if s[i] == " " and not space:
                continue
            if s[i] == " " and space:
                break
            if s[i].isalpha():
                c += 1
                space = True
        
        return c