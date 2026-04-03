class MyHashSet:

    def __init__(self):
        self.size = 1_000_000
        self.hashset = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.hashset[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i in range(len(self.hashset[idx])):
            if self.hashset[idx][i] == key:
                self.hashset[idx][i] = -1

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        for i in range(len(self.hashset[idx])):
            if self.hashset[idx][i] == key:
                return True
        return False

    def _hash(self, key: int) -> int:
        return key % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)