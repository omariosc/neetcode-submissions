class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        length = len(points)

        def manhattan(a: List[int], b: List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        for a in points:
            for b in points:
                # if a != b: # Redundant since 0 cost will not add to minimum cost
                adj[(a[0], a[1])].append((b, manhattan(a,b)))
        
        minimumCost, pq, visited = 0, [(0, (points[0][0], points[0][1]))], set()
        while pq and len(visited) < length:
            cost, (x, y) = heapq.heappop(pq)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            minimumCost += cost
            for (a,b), cost in adj[(x,y)]:
                if (a,b) not in visited:
                    heapq.heappush(pq, (cost, (a,b)))
        
        return minimumCost if len(visited) == length else -1