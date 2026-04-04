class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        maxTurbulent, currTurbulent = arr[0], 0

        # Odds are larger
        for k in range(1, arr):
            if i % 2 == 1 and arr[k-1] < arr[k] > arr[k+1]:
                currTurbulent += arr[k]
                maxTurbulent = max(maxTurbulent, currTurbulent)
            elif i % 2 == 0 and arr[k-1] > arr[k] < arr[k+1]:
                currTurbulent += arr[k]
                maxTurbulent = max(maxTurbulent, currTurbulent)
            else:
                currTurbulent = 0
        # Evens are larger
        for k in range(1, arr):
            if i % 2 == 1 and arr[k-1] < arr[k] > arr[k+1]:
                currTurbulent += arr[k]
                maxTurbulent = max(maxTurbulent, currTurbulent)
            elif i % 2 == 0 and arr[k-1] > arr[k] < arr[k+1]:
                currTurbulent += arr[k]
                maxTurbulent = max(maxTurbulent, currTurbulent)
            else:
                currTurbulent = 0

        return maxTurbulent