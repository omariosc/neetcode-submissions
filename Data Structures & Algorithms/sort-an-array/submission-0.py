class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr: List[int], L: int, R: int) -> List[int]:
            if L == R:
                return [arr[L]]
            
            M = (L + R) // 2
            l = mergeSort(arr, L, M)
            r = mergeSort(arr, M+1, R)
            return merge(l, r)

        def merge(a: List[int], b: List[int]) -> List[int]:
            res = []
            l = r = 0
            while l < len(a) and r < len(b):
                if a[l] < b[r]:
                    res.append(a[l])
                    l += 1
                else:
                    res.append(b[r])
                    r += 1
            if l < len(a):
                res.extend(a[l:])
            if r < len(b):
                res.extend(b[r:])
            return res

        return mergeSort(nums, 0, len(nums) - 1)