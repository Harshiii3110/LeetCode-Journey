class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    queue = deque([(r, c)])
                    grid[r][c] = '0'
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy
                            if (0 <= nx < rows and
                                0 <= ny < cols and
                                grid[nx][ny] == '1'):
                                grid[nx][ny] = '0'
                                queue.append((nx, ny))
        return islands        
