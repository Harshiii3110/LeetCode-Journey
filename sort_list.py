# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # Step 1: Find the middle
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        prev.next = None

        # Step 2: Sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        if left:
            current.next = left
        else:
            current.next = right

        return dummy.next
