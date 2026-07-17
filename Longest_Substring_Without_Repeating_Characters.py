class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charIndex = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if s[right] in charIndex and charIndex[s[right]] >= left:
                left = charIndex[s[right]] + 1
            charIndex[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest        
