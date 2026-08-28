class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        target = n * n
        def get_position(num):
            # Convert square number to board coordinates
            row = n - 1 - (num - 1) // n
            col = (num - 1) % n
            # Every alternate row is reversed
            if ((n - 1 - row) % 2) == 1:
                col = n - 1 - col
            return row, col
        queue = deque([(1, 0)])
        visited = {1}
        while queue:
            curr, moves = queue.popleft()
            if curr == target:
                return moves
            for next_pos in range(curr + 1, min(curr + 6, target) + 1):
                r, c = get_position(next_pos)
                # Take snake/ladder only once
                destination = board[r][c]
                if destination != -1:
                    next_pos = destination
                if next_pos == target:
                    return moves + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        return -1  
