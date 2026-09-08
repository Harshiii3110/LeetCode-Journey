class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = {}
        # Count elements in nums1
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        result = []
        # Find common elements using nums2
        for num in nums2:
            if freq.get(num, 0) > 0:
                result.append(num)
                freq[num] -= 1
        return result
