class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:    
            self.graph[dst] = []
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False
        
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False

        q = collections.deque()
        visited = set()
        q.append(src)
        while q:
            node = q.popleft()
            if node == dst:
                return True
            for neighbour in self.graph[node]:
                q.append(neighbour)
                visited.add(neighbour)
        return False
