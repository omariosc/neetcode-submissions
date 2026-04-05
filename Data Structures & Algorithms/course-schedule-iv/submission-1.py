class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = collections.defaultdict(list)
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        
        visited = set()

        def dfs(course, path):
            if course in path: return False
            if course in visited: return True

            path.add(course)
            for neighbour in adjList[course]:
                if not dfs(neighbour, path): return False
            path.remove(course)
            visited.add(course)
            return True

        res = []
        for prereq, course in queries:
            path = set()
            if not dfs(course, path): 
                res.append(False)
                continue
            if prereq in visited:
                res.append(True)
            else:
                res.append(False)
        return res