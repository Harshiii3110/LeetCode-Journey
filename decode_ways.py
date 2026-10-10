class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n= len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            # One-digit decoding
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # Two-digit decoding
            if i >= 2:
                two_digit = int(s[i - 2:i])
                if 10 <= two_digit <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]
