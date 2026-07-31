class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9 # Height / Width of our board
        
        for i in range(N): # Rows
            row, col = set(), set()
            for j in range(N):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
        
        left, right, center = set(), set(), set()     
        for i in range(3):
            for j in range(3):
                if board[i][j] != '.':
                    if board[i][j] in left:
                        return False
                    left.add(board[i][j])
            for j in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in center:
                        return False
                    center.add(board[i][j])
            for j in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in right:
                        return False
                    right.add(board[i][j])

        left1, right1, center1 = set(), set(), set()     
        for i in range(3, 6):
            for j in range(3):
                if board[i][j] != '.':
                    if board[i][j] in left1:
                        return False
                    left1.add(board[i][j])
            for j in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in center1:
                        return False
                    center1.add(board[i][j])
            for j in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in right1:
                        return False
                    right1.add(board[i][j])

        left2, right2, center2 = set(), set(), set()     
        for i in range(6, 9):
            for j in range(3):
                if board[i][j] != '.':
                    if board[i][j] in left2:
                        return False
                    left2.add(board[i][j])
            for j in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in center2:
                        return False
                    center2.add(board[i][j])
            for j in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in right2:
                        return False
                    right2.add(board[i][j])
        return True