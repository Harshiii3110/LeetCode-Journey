class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    queue = deque([(r, c)])
                    grid[r][c] = 0
                    while queue:
                        x, y = queue.popleft()
                        area += 1
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                                grid[nx][ny] = 0
                                queue.append((nx, ny))
                    max_area = max(max_area, area)
        return max_area       
