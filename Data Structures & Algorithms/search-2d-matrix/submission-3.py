class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid_r = top + (bot - top) // 2

            if matrix[mid_r][0] <= target and matrix[mid_r][-1] >= target:
                break
            elif matrix[mid_r][0] > target:
                bot = mid_r - 1
            else:
                top = mid_r + 1

        print(mid_r)

        l, r = 0, len(matrix[mid_r]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[mid_r][m] == target:
                return True
            elif matrix[mid_r][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False

        
            
            