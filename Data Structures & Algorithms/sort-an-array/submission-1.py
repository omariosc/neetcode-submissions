class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr: List[int], L: int, R: int) -> List[int]:
            if L == R:
                return arr
            
            M = (L + R) // 2
            mergeSort(arr, L, M)
            mergeSort(arr, M+1, R)
            merge(arr, L, M, R)
            return arr

        def merge(arr: List[int], L: int, M: int, R: int) -> List[int]:
            a, b = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0
            while j < len(a) and k < len(b):
                if a[j] <= b[k]:
                    arr[i] = a[j]
                    j += 1
                else:
                    arr[i] = b[k]
                    k += 1
                i += 1

            while j < len(a):
                arr[i] = a[j]
                j += 1
                i += 1
            while k < len(b):
                arr[i] = b[k]
                k += 1
                i += 1

        return mergeSort(nums, 0, len(nums) - 1)