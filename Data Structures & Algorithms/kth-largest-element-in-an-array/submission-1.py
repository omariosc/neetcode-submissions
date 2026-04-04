class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap(nums[:k])
        for num in nums[k]:
            if num > heap.peek():
                heap.pop()
                heap.push(num)
        return heap.peek()

class Heap:
    def __init__(self, nums: List[int]) -> None:
        self.heap = [None] + nums
        for i in range(len(self.heap)//2, 0, -1):
            self._sift_down(i)
    
    def __len__(self) -> int:
        return len(self.heap)-1
    
    def peek(self) -> int | None:
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return None

    def _sift_down(self, i: int) -> None:
        n = len(self.heap)
        while 2*i < n:
            smallest = 2*i
            if 2*i+1 < n and self.heap[smallest+1] < self.heap[smallest]:
                smallest = 2*i+1
            if self.heap[i] <= self.heap[smallest]:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def pop(self) -> int | None:
        if len(self.heap) < 1:
            return None
        root = self.heap[1]
        last_val = self.heap.pop()
        if len(self.heap) > 1:
            self.heap[1] = last_val
            self._sift_down(1)
        return root

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2