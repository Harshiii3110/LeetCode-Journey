class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = (s + s)[1:-1]
        return s in temp
