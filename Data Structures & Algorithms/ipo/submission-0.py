import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0
        for _ in range(k):
            # unlock all projects we can afford
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush_max(heap, projects[i][1])
                i += 1
            if not heap:
                break
            w += heapq.heappop_max(heap)
        return w