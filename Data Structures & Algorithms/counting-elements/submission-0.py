class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_elements = set(arr)
        count = 0
        for n in arr:
            if n + 1 in arr_elements:
                count += 1
        return count