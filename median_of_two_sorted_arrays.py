class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1
            # Elements immediately around the partitions
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == n else nums2[cut2]
            # Correct partition
            if left1 <= right2 and left2 <= right1:
                # Odd total length
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2.0
            # nums1 partition is too far right
            elif left1 > right2:
                right = cut1 - 1
            # nums1 partition is too far left
            else:
                left = cut1 + 1    
