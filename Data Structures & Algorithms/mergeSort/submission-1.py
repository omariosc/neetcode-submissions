# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        if start == end:
            return [pairs[start]]
        
        mid = start + (end-start)//2
        left = self.mergeSortHelper(pairs, start, mid)
        right = self.mergeSortHelper(pairs, mid+1, end)
        return self.merge(left, right)

    
    def merge(
        self,
        left: List[Pair],
        right: List[Pair]
    ) -> List[Pair]:

        i = j = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged