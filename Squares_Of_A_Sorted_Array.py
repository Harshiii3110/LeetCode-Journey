class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                ans[pos] = left_square
                left += 1
            else:
                ans[pos] = right_square
                right -= 1
            pos -= 1
        return ans        
