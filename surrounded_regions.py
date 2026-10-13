class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] != 'O':
                return
            board[r][c] = 'S'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        # Mark boundary-connected O cells as safe
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        # Capture surrounded regions and restore safe cells
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
