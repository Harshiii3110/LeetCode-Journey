class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(string):
            stack = []
            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack
        return build(s) == build(t)        
