class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif t == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif t == "*":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif t == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                if op1 == 0 or op2 == 0:
                    stack.append(0)
                else:
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(t))
        return int(stack[-1])