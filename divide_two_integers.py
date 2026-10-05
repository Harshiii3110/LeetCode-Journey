class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)
        # Work with positive values
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0
        # Subtract the largest possible shifted divisor each time
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple
        if negative:
            quotient = -quotient
        # Handle 32-bit overflow
        if quotient > INT_MAX:
            return INT_MAX
        if quotient < INT_MIN:
            return INT_MIN
        return quotient
