# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(0, len(pairs) - 1, pairs)
        return pairs

    def quickSortHelper(self, s, e, arr):
        if (e-s+1) <= 1:
            return arr
        pivot = e
        i = s
        j = s
        while i < e:
            if arr[i].key < arr[pivot].key:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
            i += 1
        arr[j], arr[pivot] = arr[pivot], arr[j]

        self.quickSortHelper(s, j - 1, arr)
        self.quickSortHelper(j+1, e, arr)

        