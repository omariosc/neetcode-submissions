class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for source, target, cost in edges:
            adj[source].append((target, cost))
            adj[target].append((source, cost))

        totalCost, pq, visited = 0, [(0, 0)], set()
        
        while pq and len(visited) < n:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            totalCost += cost
            visited.add(node)
            for neighbour, cost in adj[node]:
                if neighbour not in visited:
                    heapq.heappush(pq, (cost, neighbour))

        
        return totalCost if len(visited) == n else -1