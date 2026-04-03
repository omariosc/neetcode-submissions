class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        topSort, visited, path = [], set(), set()

        def dfs(course):
            if course in path: return False
            if course in visited: return True

            path.add(course)
            visited.add(course)
            for neighbour in adj[course]:
                if not dfs(neighbour): return False
            path.remove(course)
            topSort.append(course)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i): return []

        return topSort[::-1] if len(topSort) == numCourses else []