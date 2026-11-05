class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2

            if coins <= n:
                left = mid + 1
            else:
                right = mid - 1

        return right
