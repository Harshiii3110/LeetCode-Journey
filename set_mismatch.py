class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freq = [0] * (n + 1)
        for num in nums:
            freq[num] += 1
        duplicate = -1
        missing = -1
        for num in range(1, n + 1):
            if freq[num] == 2:
                duplicate = num
            elif freq[num] == 0:
                missing = num
        return [duplicate, missing]
