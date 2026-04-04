class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = collections.defaultdict(list)
        for source, target, cost in edges:
            adjList[source].append((target, cost))

        dest = {}
        pq = [(0, src)]
        while pq:
            currCost, node = heapq.heappop(pq)
            if node in dest:
                continue
            dest[node] = currCost
            for neighbour, cost in adjList[node]:
                if neighbour in dest:
                    continue
                heapq.heappush(pq, (cost + currCost, neighbour))
        for node in adjList:
            if node not in dest:
                dest[node] = -1
        return dest