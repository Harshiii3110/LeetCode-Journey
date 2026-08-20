class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        def bfs(starts, visited):
            queue = deque(starts)
            for cell in starts:
                visited.add(cell)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
        # Pacific: top row + left column
        pacific_starts = []
        for c in range(n):
            pacific_starts.append((0, c))
        for r in range(m):
            pacific_starts.append((r, 0))
        # Atlantic: bottom row + right column
        atlantic_starts = []
        for c in range(n):
            atlantic_starts.append((m - 1, c))
        for r in range(m):
            atlantic_starts.append((r, n - 1))
        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result        
