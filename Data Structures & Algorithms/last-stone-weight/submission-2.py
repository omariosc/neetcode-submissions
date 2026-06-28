class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            second_heaviest = heapq.heappop_max(stones)
            if heaviest != second_heaviest:
                heapq.heappush_max(stones, heaviest - second_heaviest)

        return stones[0] if len(stones) > 0 else 0
