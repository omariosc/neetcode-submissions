class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
 
        brackets = {")":"(","]":"[","}":"{"}

        stack = []
        for i in s:
            if i not in brackets:
                stack.append(i)
            elif len(stack) > 0 and stack[-1] == brackets[i]:
                stack.pop()
            else:
                return False

        return True if len(stack) == 0 else False