class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}

        # Build the graph
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(start, end, visited):
            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        answers = []

        for a, b in queries:
            if a not in graph or b not in graph:
                answers.append(-1.0)
            elif a == b:
                answers.append(1.0)
            else:
                answers.append(dfs(a, b, set()))

        return answers
