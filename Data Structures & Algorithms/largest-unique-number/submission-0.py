class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for n in nums:
            counts[n] += 1

        seen = []
        heapq.heapify(seen)
        for key, value in counts.items():
            if value == 1:
                heapq.heappush(seen, -key)

        if len(seen) == 0: return -1
        return -heapq.heappop(seen)