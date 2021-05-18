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
        newHead = ListNode(0)
        currentHead = newHead
        carry = 0
        
        while l1 or l2:
            x_val = 0
            if l1 is not None:
                x_val = l1.val
            y_val = 0
            if l2 is not None:
                y_val = l2.val
            
            # calculate sum
            sum = x_val + y_val + carry
            carry = sum / 10
            
            # add current to list
            currentHead.next = ListNode(sum % 10)
            currentHead = currentHead.next

            # increment two lists
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # add any elements additional
        if carry > 0:
            currentHead.next = ListNode(carry)
        
        return newHead.next
