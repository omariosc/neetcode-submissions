class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [[] for _ in range(capacity)]

    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)

        for _, node in enumerate(self.map[index]):
            if node.key == key:
                node.val = value
                return

        node = Node(key, value)
        self.map[index].append(node) 
        self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self._hash(key)

        for i, node in enumerate(self.map[index]):
            if node.key == key:
                return node.val

        return -1
        
    def remove(self, key: int) -> bool:
        index = self._hash(key)

        for i, node in enumerate(self.map[index]):
            if node.key == key:
                self.map[index].pop(i)
                self.size -= 1
                return True

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_map = self.map
        self.capacity *= 2
        self.size = 0
        self.map = [[] for _ in range(self.capacity)]
        for bucket in old_map:
            for node in bucket:
                self.insert(node.key, node.val)

    def _hash(self, key: int) -> int:
        return key % self.capacity

class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val