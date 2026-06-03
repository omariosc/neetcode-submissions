class MyHashMap:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [[] for i in range(self.bucket_size)]

    def put(self, key: int, value: int) -> None:
        i = self.hash(key)

        for idx, (k, v) in enumerate(self.buckets[i]):
            if k == key:
                self.buckets[i][idx] = (key, value)
                return
        self.buckets[i].append((key, value))

    def get(self, key: int) -> int:
        i = self.hash(key)
        if len(self.buckets[i]) > 0:
            for k, v in self.buckets[i]:
                if k == key:
                    return v
        return -1

    def remove(self, key: int) -> None:
        i = self.hash(key)
        if len(self.buckets[i]) > 0:
            for idx, (k, v) in enumerate(self.buckets[i]):
                if k == key:
                    self.buckets[i].pop(idx)


    def hash(self, key: int) -> int:
        return key % self.bucket_size 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)