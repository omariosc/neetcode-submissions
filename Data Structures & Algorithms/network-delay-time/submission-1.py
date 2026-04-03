class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = collections.defaultdict(list)
        for start, end, time in times:
            adjacencyList[start].append((end, time))

        destinations = {}
        priority_queue = [(0, k)]
        while priority_queue:
            distance, node = heapq.heappop(priority_queue)
            if node not in destinations:
                destinations[node] = distance
                for neighbour, time in adjacencyList[node]:
                    if neighbour not in destinations:
                        heapq.heappush(priority_queue, (distance + time, neighbour))

        return max(destinations.values()) if len(destinations) == n else -1