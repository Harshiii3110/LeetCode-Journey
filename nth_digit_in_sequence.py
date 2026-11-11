class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_length = 1
        start = 1
        count = 9

        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            start *= 10
            count *= 10

        number = start + (n - 1) // digit_length
        index = (n - 1) % digit_length

        return int(str(number)[index])
