class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        maxTurbulent, currTurbulent = 1, 1

        # Odds are larger
        for k in range(len(arr)):
            if k > 0 and ((k % 2 == 1 and arr[k-1] < arr[k]) or (k % 2 == 0 and arr[k-1] > arr[k])):
                currTurbulent += 1
            else:
                currTurbulent = 1
            maxTurbulent = max(maxTurbulent, currTurbulent)
        
        currTurbulent = 1
        # Evens are larger
        for k in range(len(arr)):
            if k > 0 and ((k % 2 == 0 and arr[k-1] < arr[k]) or (k % 2 == 1 and arr[k-1] > arr[k])):
                currTurbulent += 1
            else:
                currTurbulent = 1
            maxTurbulent = max(maxTurbulent, currTurbulent)

        return maxTurbulent