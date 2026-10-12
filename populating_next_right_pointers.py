"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        leftmost = root
        while leftmost.left:
            current = leftmost
            while current:
                # Connect siblings
                current.left.next = current.right
                # Connect children of neighboring parents
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            leftmost = leftmost.left
        return root
