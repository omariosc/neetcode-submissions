# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSortHelper(arr, s, e):
            if e - s <= 0:
                return arr

            l = s
            pivot = arr[e]
            for i in range(s, e):
                if arr[i].key < pivot.key:
                    arr[i], arr[l] = arr[l], arr[i]
                    l += 1
            
            arr[e], arr[l] = arr[l], arr[e]

            quickSortHelper(arr, s, l - 1)
            quickSortHelper(arr, l + 1, e)

            return arr

        return quickSortHelper(pairs, 0, len(pairs)-1)