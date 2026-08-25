class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        # Minimum cost to connect each point to the MST
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = [False] * n
        total_cost = 0
        for _ in range(n):
            # Find the unvisited point with minimum connection cost
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            visited[u] = True
            total_cost += min_dist[u]
            # Update distances of the remaining points
            for v in range(n):
                if not visited[v]:
                    distance = abs(points[u][0] - points[v][0]) + \
                               abs(points[u][1] - points[v][1])
                    min_dist[v] = min(min_dist[v], distance)
        return total_cost        
