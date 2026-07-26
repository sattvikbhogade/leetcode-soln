class Solution:
    def getMaxRowIndex(self, mat, rows, cols, col):
        maxVal = -1 
        rowIndex = -1 
        for i in range(rows):
            if mat[i][col] > maxVal:
                maxVal = mat[i][col]
                rowIndex = i 
        return rowIndex
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        low = 0 
        high = cols - 1 
        
        while low <= high:
            mid = (low + high) // 2 
            
            maxRowIndex = self.getMaxRowIndex(mat, rows, cols, mid)
            
            left = mat[maxRowIndex][mid - 1] if mid - 1 >= 0 else -1
            right = mat[maxRowIndex][mid + 1] if mid + 1 < cols else -1
            
            if mat[maxRowIndex][mid] > left and mat[maxRowIndex] [mid] > right:
                return [maxRowIndex, mid]
            elif mat[maxRowIndex][mid] < left:
                high = mid - 1 
            else:
                low = mid + 1 
        return [-1, -1]