# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return 0
    
        # map to store encoutnered nodes in A
        map = {}
        
        # add nodes of A to map
        while headA:
            map[headA] = 1
            headA = headA.next
        
        # check if nodeB is in map
        while headB:
            if headB in map:
                return headB
            headB = headB.next
        
        # no intersections found
        return None
