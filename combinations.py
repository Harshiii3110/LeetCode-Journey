class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def backtrack(start):
            if len(path) == k:
                result.append(path[:])
                return

            remaining = k - len(path)

            for num in range(start, n - remaining + 2):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return result
