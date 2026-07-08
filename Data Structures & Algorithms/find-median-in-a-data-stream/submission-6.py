class MedianFinder:
    
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))
        if len(self.large) > len(self.small):
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        return (self.small[0] + self.large[0]) / 2