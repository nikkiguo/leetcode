# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        left = head
        right = head

        while right and right.next:
            left = left.next
            right = right.next.next

            if left == right:
                return True
        return False
        