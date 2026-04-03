class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            second_heaviest = heapq.heappop(stones)

            if heaviest < second_heaviest:
                heapq.heappush(stones, heaviest - second_heaviest)
            elif heaviest > second_heaviest:
                heapq.heappush(stones, second_heaviest - heaviest)


        return -stones[0] if len(stones) > 0 else 0
