class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        # Smallest lexical destination first
        for src in graph:
            graph[src].sort(reverse=True)
        route = []
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            route.append(airport)
        dfs("JFK")
        return route[::-1]        
