class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        cols = len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) == (rows - 1, cols - 1):
                return effort
            if effort > dist[r][c]:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, diff)
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0
