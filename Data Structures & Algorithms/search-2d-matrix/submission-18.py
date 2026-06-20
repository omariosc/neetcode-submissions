class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        row = -1

        while top <= bottom:
            mid = top + (bottom-top)//2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                row = mid
                break
        
        if row == -1:
            return False

        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = left + (right-left)//2
            if target < matrix[row][mid]:
                right = mid-1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True # matrix[row][mid]

        return False