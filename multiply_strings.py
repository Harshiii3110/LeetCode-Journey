class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                pos1 = i + j
                pos2 = i + j + 1
                total = product + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10
        # Remove leading zeros
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1
        return ''.join(str(x) for x in result[start:])
