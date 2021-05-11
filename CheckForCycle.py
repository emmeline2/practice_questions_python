class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # check base case
        if (head is None) or head.next is None:
            return False
        
        slow = head
        fast = head.next
        
        # Slow is one step behind fast, if fast ever equals
        # slow that means we have gone in a circle.
        
        while slow != fast:
            if fast is None or fast.next is None:
                # Reached the end without cycles
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
