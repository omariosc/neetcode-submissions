class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        currSum = 0
        L = 0

        for R in range(0, len(arr)):
            currLength = R - L + 1
            currSum += arr[R]
            if currLength > k:
                currSum -= arr[L]
                L += 1
                currLength -= 1
            if currLength == k and currSum >= threshold * k:
                res += 1

        return res