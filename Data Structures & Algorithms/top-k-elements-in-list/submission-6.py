from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        return [key for key, _ in hm.most_common(k)]
        