class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_del = [i for i in row if i != "."]
            if len(row_del) != len(set(row_del)):
                return False
        
        transposed_board = []
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(board[j][i])
            transposed_board.append(tmp)

        for col in transposed_board:
            col_del = [i for i in col if i != "."]
            if len(col_del) != len(set(col_del)):
                return False

        squared_board = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                squared_board[(i//3)*3 + (j//3)].append(board[i][j])
        for box in squared_board:
            col_del = [i for i in box if i != "."]
            if len(col_del) != len(set(col_del)):
                return False 
            
        return True
        