class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        nxt = {}
        for num in nums2:
            while stack and num > stack[-1]:
                nxt[stack.pop()] = num
            stack.append(num)
        ans = []
        for num in nums1:
            ans.append(nxt.get(num, -1))
        return ans        
