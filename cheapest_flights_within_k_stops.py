class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float('inf')
        # At most k stops means at most k + 1 flights
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            new_dist = dist[:]
            for u, v, price in flights:
                if dist[u] != INF:
                    new_dist[v] = min(
                        new_dist[v],
                        dist[u] + price
                    )
            dist = new_dist
        return -1 if dist[dst] == INF else dist[dst] 
