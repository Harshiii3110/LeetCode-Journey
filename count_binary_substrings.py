class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        previous_count = 0
        current_count = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_count += 1
            else:
                result += min(previous_count, current_count)
                previous_count = current_count
                current_count = 1

        result += min(previous_count, current_count)

        return result
