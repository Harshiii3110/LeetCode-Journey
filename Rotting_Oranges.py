class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh = 0
        # Find all rotten and fresh oranges
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while queue and fresh > 0:
            # Process all oranges that are rotten
            # at the beginning of this minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr, nc))
            minutes += 1
        if fresh > 0:
            return -1
        return minutes        
