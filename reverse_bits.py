class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            # Get the last bit
            bit = n & 1
            # Add it to result
            result = (result << 1) | bit
            # Remove the last bit from n
            n >>= 1
        return result
