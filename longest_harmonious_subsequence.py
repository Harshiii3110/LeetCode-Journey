class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        answer = 0
        for num in freq:
            if num + 1 in freq:
                answer = max(answer, freq[num] + freq[num + 1])
        return answer 
