class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = collections.defaultdict(list)
        for source, target, cost in edges:
            adjList[source].append((target, cost))

        shortest = {}
        pq = [(0, src)]
        while pq:
            currCost, node = heapq.heappop(pq)
            if node in shortest:
                continue
            shortest[node] = currCost
            for neighbour, cost in adjList[node]:
                if neighbour not in shortest:
                    heapq.heappush(pq, (cost + currCost, neighbour))
        
        for node in range(n):
            if node not in shortest:
                shortest[node] = -1
        
        return shortest