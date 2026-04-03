class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        if self.large and self.small[0] > self.large[0]:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        else:
            return (self.small[0] + self.large[0]) / 2