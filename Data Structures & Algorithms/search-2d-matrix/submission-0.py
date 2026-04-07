class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n, row in enumerate(matrix):
            if target in row:
                return True
            
        return False
            