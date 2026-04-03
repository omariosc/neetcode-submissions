class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r = len(arr)-1
        maximum = arr[-1]
        arr[-1] = -1
        while r > 0:
            r -= 1
            curr = arr[r]
            arr[r] = maximum
            maximum = max(maximum,curr)
        return arr