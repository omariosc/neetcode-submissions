class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        visited_count = 0
        minimumCost = 0
        pq = [(0, 0)]

        def manhattan(a: List[int], b: List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        while visited_count < n:
            cost, node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            visited_count += 1
            minimumCost += cost
            for neighbour in range(n):
                if not visited[neighbour]:
                    dist = manhattan(points[node], points[neighbour])
                    heapq.heappush(pq, (dist, neighbour))
        
        return minimumCost if all(visited) else -1