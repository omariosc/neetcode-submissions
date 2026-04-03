class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t))
        
        dest = {}
        pq = [(0,k)]
        while pq:
            d, v = heapq.heappop(pq)
            if v not in dest:
                dest[v] = d
                for i, t in adj[v]:
                    if i not in dest:
                        heapq.heappush(pq, (d+t, i))
        
        return max(dest.values()) if len(dest) == n else -1