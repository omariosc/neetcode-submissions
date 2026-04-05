class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = collections.defaultdict(list)
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        
        def dfs(course, path, visited):
            if course in path: return False
            if course in visited: return True

            path.add(course)
            for neighbour in adjList[course]:
                if not dfs(neighbour, path, visited): return False
            path.remove(course)
            visited.add(course)
            return True

        res = []
        for prereq, course in queries:
            visited, path = set(), set()
            if not dfs(course, path, visited): 
                res.append(False)
                continue
            if prereq in visited:
                res.append(True)
            else:
                res.append(False)
        return res