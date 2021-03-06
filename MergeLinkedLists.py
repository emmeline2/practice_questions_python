class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_head = ListNode(0)  
        cur = temp_head

        while l1 and l2:  
            if l1.val <= l2.val:  
                cur.next = l1  
                l1 = l1.next  
            else:  
                cur.next = l2  
                l2 = l2.next  
            cur = cur.next
        
        # try to assign l1 but if null assign l2
        cur.next = l1 or l2  
  
        return temp_head.next  
