class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [str(i) for i in range(1, n + 1)]
        # Precompute factorials
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        k -= 1
        result = []
        for i in range(n, 0, -1):
            block_size = factorial[i - 1]
            index = k // block_size
            result.append(numbers[index])
            numbers.pop(index)
            k %= block_size
        return ''.join(result)
