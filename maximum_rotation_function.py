class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        total_sum = sum(nums)

        current = 0
        for i in range(n):
            current += i * nums[i]

        max_value = current

        for k in range(1, n):
            current = current + total_sum - n * nums[n-k]
            max_value = max(max_value, current)

        return max_value
