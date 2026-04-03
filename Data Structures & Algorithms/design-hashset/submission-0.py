class MyHashSet:

    def __init__(self):
        self.size = 1_000_000
        self.hashset = [-1] * self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.hashset[idx] = key

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.hashset[idx] = -1

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return False if self.hashset[idx] == -1 else True
        

    def _hash(self, key: int) -> int:
        return key % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)