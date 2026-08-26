class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        # -1 = not colored
        #  0 and 1 = two different groups
        color = [-1] * n
        for start in range(n):
            # Graph may be disconnected
            if color[start] != -1:
                continue
            queue = [start]
            color[start] = 0
            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    # If v is not colored, give it the opposite color
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    # Adjacent nodes cannot have the same color
                    elif color[v] == color[u]:
                        return False
        return True        
