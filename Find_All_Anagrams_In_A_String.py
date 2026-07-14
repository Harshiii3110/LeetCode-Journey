class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        pCount = [0] * 26
        window = [0] * 26
        for ch in p:
            pCount[ord(ch) - ord('a')] += 1
        for i in range(len(p)):
            window[ord(s[i]) - ord('a')] += 1
        ans = []
        if window == pCount:
            ans.append(0)
        for i in range(len(p), len(s)):
            window[ord(s[i]) - ord('a')] += 1
            window[ord(s[i - len(p)]) - ord('a')] -= 1
            if window == pCount:
                ans.append(i - len(p) + 1)
        return ans        
