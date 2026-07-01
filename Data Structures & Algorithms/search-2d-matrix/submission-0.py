class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        ROWS  , COLS = len(mat) , len(mat[0])

        # first i have to check from top to bottom
        # for each middle i have to check if it lies within column range

        top = 0
        bottom = ROWS - 1

        ans_row = -1
        ans_col = -1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if mat[mid_row][0] <= target <= mat[mid_row][-1]:
                ans_row = mid_row
                break
            elif mat[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1
    
        if ans_row == -1:
            return False
        left = 0
        right = COLS - 1
        while left <= right:
            mid_col = (left + right) // 2
            if mat[ans_row][mid_col] == target:
                return True
            elif mat[ans_row][mid_col] > target:
                right = mid_col - 1
            else:
                left = mid_col + 1
        return False

