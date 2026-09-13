class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        current = []
        def backtrack(start):
            result.append(current[:])
            for i in range(start, len(nums)):
                # Skip duplicate elements at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()
        backtrack(0)
        return result
