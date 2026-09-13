class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current = []
        def backtrack(index):
            if index == len(nums):
                result.append(current[:])
                return
            # Include nums[index]
            current.append(nums[index])
            backtrack(index + 1)
            # Exclude nums[index]
            current.pop()
            backtrack(index + 1)
        backtrack(0)
        return result
