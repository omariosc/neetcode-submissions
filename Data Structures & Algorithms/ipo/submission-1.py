class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        # Sort projects by capital first so that can iterate over all the ones we can afford.
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0

        # We only need to take k projects
        for _ in range(k):
            #  If there are still projects to take from, and we can afford to start it
            while i < len(projects) and projects[i][0] <= w:
                # Add the profit to our max heap
                heapq.heappush_max(heap, projects[i][1])
                i += 1
            # If no available projects, then we can't make any more profit
            if not heap:
                break
            # We take the project with highest profit, from heap (projects we can afford)
            w += heapq.heappop_max(heap)

        return w