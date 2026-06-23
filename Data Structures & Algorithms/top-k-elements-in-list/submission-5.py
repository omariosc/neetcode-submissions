from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [n for n, _ in list(sorted(counter.items(), key=lambda x: x[1], reverse=True))[:k]]
        