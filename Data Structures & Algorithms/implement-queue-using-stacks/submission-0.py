class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        if self.empty():
            self.a.append(x)
        else:
            self.b.append(x)

    def pop(self) -> int:
        val = self.a.pop()
        if len(self.a) == 0:
            while len(self.b) > 0:
                self.a.append(self.b.pop())
        return val

    def peek(self) -> int:
        return self.a[-1]

    def empty(self) -> bool:
        return len(self.a) == 0 and len(self.b) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()