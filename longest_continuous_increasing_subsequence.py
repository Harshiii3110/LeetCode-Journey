class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 1
        answer = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                current = 1
            answer = max(answer, current)
        return answer
