class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        while top <= bottom:
            m = (top+bottom)//2
            row = matrix[m]
            if target >= row[0] and target <= row[-1]:
                while left <= right:
                    mid = (left+right)//2
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        left = mid + 1
                    elif target < row[mid]:
                        right = mid - 1
                return False 
            elif target > row[-1]:
                top = m + 1
            elif target < row[0]:
                bottom = m - 1 

        return False

