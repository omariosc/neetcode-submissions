from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.tail = None

class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] += 1

    def pop(self) -> int:
        most = max(self.freq.values())
        tmp = []
        while self.stack and self.freq[self.stack[-1]] != most:
            tmp.append(self.stack.pop())
        res = -1
        if self.stack and self.freq[self.stack[-1]] == most:
            res = self.stack.pop()
            self.freq[res] -= 1
        for i in tmp:
            self.stack.append(i)
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()