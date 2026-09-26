class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        unique_types = len(set(candyType))
        return min(unique_types, n // 2)
