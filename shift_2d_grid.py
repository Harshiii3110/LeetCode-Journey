class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        arr = []
        for row in grid:
            arr.extend(row)
        total = m * n
        k = k % total
        arr = arr[-k:] + arr[:-k] if k != 0 else arr
        result = []
        for i in range(0, total, n):
            result.append(arr[i:i + n])
        return result
