class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        min_rows = m
        min_cols = n
        for a, b in ops:
            min_rows = min(min_rows, a)
            min_cols = min(min_cols, b)
        return min_rows * min_cols
