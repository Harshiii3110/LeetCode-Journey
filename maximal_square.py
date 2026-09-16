class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * (n + 1)
        max_side = 0
        prev = 0
        for i in range(m):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i][j - 1] == '1':
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return max_side * max_side
