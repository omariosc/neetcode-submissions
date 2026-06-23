class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr) - 1
        while L <= R:
            M = (L + R) // 2
            if x < arr[M]:
                R = M - 1
            elif x > arr[M]:
                L = M + 1
            else:
                L = R = M
                break
        
        L, R = R, R + 1
        res = []
        while len(res) < k:
            if L >= 0 and R < len(arr):
                if abs(arr[L]-x) <= abs(arr[R]-x):
                    res.append(arr[L])
                    L -= 1
                else:
                    res.append(arr[R])
                    R += 1
            elif L >= 0:
                res.append(arr[L])
                L -= 1
            else:
                res.append(arr[R])
                R += 1
        return sorted(res)