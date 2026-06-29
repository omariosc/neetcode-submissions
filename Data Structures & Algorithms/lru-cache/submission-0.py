class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.LRU = Node(-1)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(key)
        self.addMRU(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        elif len(self.cache) >= self.capacity:
            self.removeLRU()
        
        self.cache[key] = value
        self.addMRU(key)


    def addMRU(self, key: int) -> None:
        cur = self.LRU
        while cur and cur.tail:
            cur = cur.tail
        cur.tail = Node(key)

    def removeLRU(self) -> None:
        lru_key = self.LRU.tail.val
        del self.cache[lru_key]
        self.LRU.tail = self.LRU.tail.tail

    def remove(self, key: int) -> None:
        cur = self.LRU
        while cur and cur.tail:
            if cur.tail.val == key:
                cur.tail = cur.tail.tail
                break
            cur = cur.tail


class Node:
    def __init__(self, val: int):
        self.val = val
        self.tail = None