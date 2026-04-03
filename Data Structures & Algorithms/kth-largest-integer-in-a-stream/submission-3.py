class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

class Heap:
    def __init__(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        if len(nums) > 1:
            first_parent = (len(self.heap)-1) // 2
            self.balance(first_parent)

    def balance(self, curr: int):
        n = len(self.heap)
        while curr > 0:
            i = curr
            while 2*i < n:
                if 2*i+1 < n and self.heap[2*i+1] < self.heap[2*i] and self.heap[2*i+1] < self.heap[i]:
                    self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                    i = 2*i+1
                elif self.heap[i] > self.heap[2*i]:
                    self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                    i = 2*i
                else:
                    break
            curr -= 1

    def push(self, val: int) -> None:
        self.heap.append(val)
        parent = len(self.heap) // 2
        new = -1
        while self.heap[new] < self.heap[parent] and parent > 0:
            self.heap[new], self.heap[parent] = self.heap[parent], self.heap[new]
            parent //= 2

    def pop(self) -> int:
        res = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.balance(1)
        return res