class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        first = {}
        last = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            frequency[num] = frequency.get(num, 0) + 1
        degree = max(frequency.values())
        answer = len(nums)
        for num in frequency:
            if frequency[num] == degree:
                length = last[num] - first[num] + 1
                answer = min(answer, length)
        return answer
