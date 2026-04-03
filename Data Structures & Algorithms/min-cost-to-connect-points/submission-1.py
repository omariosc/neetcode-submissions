class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minimumCost = 0
        pq = [(0, 0)]
        visited = set()

        def manhattan(a: List[int], b: List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        while len(visited) < n:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            minimumCost += cost
            for neighbour in range(n):
                if neighbour not in visited:
                    dist = manhattan(points[node], points[neighbour])
                    heapq.heappush(pq, (dist, neighbour))
        
        return minimumCost if len(visited) == n else -1