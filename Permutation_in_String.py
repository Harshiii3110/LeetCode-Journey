class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        # Frequency of s1 and first window of s2
        for i in range(n):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        if freq1 == freq2:
            return True
        # Slide the window
        for i in range(n, m):
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i - n]) - ord('a')] -= 1
            if freq1 == freq2:
                return True
        return False        
