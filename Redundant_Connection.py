class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []        
