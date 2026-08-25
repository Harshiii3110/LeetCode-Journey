class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # min-heap: (maximum elevation encountered, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            time, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True
            # Reached bottom-right
            if r == n - 1 and c == n - 1:
                return time
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (new_time, nr, nc))
        return -1        
