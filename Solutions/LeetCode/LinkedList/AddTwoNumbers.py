# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr_l1 = l1
        curr_l2 = l2

        result = ListNode()
        curr_res = result
        carry = 0

        while curr_l1 or curr_l2:
            if curr_l1 and curr_l2:
                val = curr_l1.val + curr_l2.val + carry
                if val >= 10:
                    carry = 1
                    val -= 10
                else:
                    carry = 0
                curr_l1 = curr_l1.next
                curr_l2 = curr_l2.next
            elif curr_l1 and not curr_l2:
                val = curr_l1.val + carry
                if val >= 10:
                    carry = 1
                    val -= 10
                else:
                    carry = 0
                curr_l1 = curr_l1.next
            else:
                val = curr_l2.val + carry
                if val >= 10:
                    carry = 1
                    val -= 10
                else:
                    carry = 0
                curr_l2 = curr_l2.next
        
            curr_res.next = ListNode(val)
            curr_res = curr_res.next
        
        if carry == 1:
            curr_res.next = ListNode(1)
            
        return result.next

            

     

        

            
        