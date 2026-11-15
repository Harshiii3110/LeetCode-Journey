class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in freq:
            if freq[ch] < k:
                parts = s.split(ch)

                return max(
                    self.longestSubstring(part, k)
                    for part in parts
                )

        return len(s)
