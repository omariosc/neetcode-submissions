class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n+1)
        for i in range(n+1):
            tmp = i
            while tmp > 0:
                if tmp & 1 == 1:
                    arr[i] += 1
                tmp >>= 1
        return arr