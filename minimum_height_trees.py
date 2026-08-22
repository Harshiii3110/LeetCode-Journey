class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        queue = deque()
        # Add all leaf nodes
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        remaining = n
        # Remove leaves layer by layer
        while remaining > 2:
            leaf_count = len(queue)
            remaining -= leaf_count
            for _ in range(leaf_count):
                leaf = queue.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        return list(queue)        
