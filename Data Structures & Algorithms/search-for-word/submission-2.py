class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def helper(r, c, idx):
            if idx == len(word):
                return True
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited or board[r][c] != word[idx]:
                return False
            
            visited.add((r, c))
            if helper(r + 1, c, idx + 1): return True
            if helper(r, c + 1, idx + 1): return True
            if helper(r - 1, c, idx + 1): return True
            if helper(r, c - 1, idx + 1): return True
            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if helper(r, c, 0):
                    return True

        return False