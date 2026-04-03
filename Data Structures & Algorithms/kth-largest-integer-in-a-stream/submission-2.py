class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = Heap(nums)
        while len(self.heap) - 1 > k:
            self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if len(self.heap) - 1 > self.k:
            self.heap.pop()
        return self.heap.peek()
        
class Heap:
    def __init__(self, nums):
        self.heap = [None] + nums
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self._sift_down(i)
    
    def __len__(self) -> int:
        return len(self.heap)

    def peek(self) -> int:
        return self.heap[1]

    def _sift_down(self, i) -> None:
        n = len(self.heap)
        while 2*i < n:
            smallest = 2*i
            if 2*i+1 < n and self.heap[2*i+1] < self.heap[smallest]:
                smallest = 2*i+1
            if self.heap[i] <= self.heap[smallest]:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def push(self, val) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return None
        root = self.heap[1]
        last_val = self.heap.pop()
        if len(self.heap) > 1:
            self.heap[1] = last_val
            self._sift_down(1)
        return root