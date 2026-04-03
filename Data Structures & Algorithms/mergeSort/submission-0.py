# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        n = len(pairs)
        m = n // 2
        l = self.mergeSort(pairs[:m])
        r = self.mergeSort(pairs[m:])
        return self.merge(l, r)


    def merge(self, l, r):
        lenL, lenR = len(l), len(r)
        if lenL == 0:
            return r
        if lenR == 0:
            return l
        arr, i, j = [], 0, 0
        while i < lenL and j < lenR:
            if l[i].key <= r[j].key:
                arr.append(l[i])
                i += 1
            else:
                arr.append(r[j])
                j += 1
        
        arr.extend(l[i:])
        arr.extend(r[j:])
        return arr
