class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        diff = (alice_total - bob_total) // 2
        bob_set = set(bobSizes)
        for a in aliceSizes:
            b = a - diff
            if b in bob_set:
                return [a, b]
