class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = 0
        currSum = sum(arr[:k-1])
        for R in range(k-1, len(arr)):
            currSum += arr[R]
            res += currSum >= threshold
            currSum -= arr[R - k + 1]
        return res