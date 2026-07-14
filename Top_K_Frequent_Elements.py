class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans        
