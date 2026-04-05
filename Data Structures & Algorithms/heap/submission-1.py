class MinHeap:
    
    def __init__(self):
        self.heap = [None]

    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap) - 1
        while i > 1 and self.heap[i // 2] > self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        
        if len(self.heap) == 2:
            return self.heap.pop()
        
        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.balance(1)
        
        return root

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [None] + nums
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self.balance(i)
        
    def balance(self, i: int) -> None:
        while 2*i < len(self.heap):
            current = 2*i
            if len(self.heap) > (current + 1) and (self.heap[current + 1] < self.heap[current]):
                current += 1
            if self.heap[i] <= self.heap[current]:
                break
            self.heap[current], self.heap[i] = self.heap[i], self.heap[current]
            i = current
        