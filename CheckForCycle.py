class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # check base case
        if (head is None) or head.next is None:
            return False
        
        # create set for seen nodes
        nodes_seen = set()
        
        while head is not None:
            if head in nodes_seen: 
                return True
            nodes_seen.add(head)
            head = head.next
        
        return False
