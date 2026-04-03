class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = collections.defaultdict(list)
        for prob, (start, end) in zip(succProb, edges):
            adjList[start].append((end, prob))
            adjList[end].append((start, prob))

        dest = {}
        pq = [(1, start_node)]
        while pq:
            currProb, node = heapq.heappop_max(pq)
            # if node == end_node:
            #     return currProb
            if node in dest:
                continue
            dest[node] = currProb
            for neighbour, prob in adjList[node]:
                if neighbour not in dest:
                    heapq.heappush_max(pq, (prob*currProb, neighbour))
        
        return dest[end_node] if end_node in dest else 0