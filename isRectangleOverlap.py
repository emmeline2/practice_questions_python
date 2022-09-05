class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int], [x1, y2, x2, y2]
        :type rec2: List[int], [x1, y2, x2, y2]
        :rtype: bool
        """
        
        # to the left or right
        if rec2[0] >= rec1[2]:
            return False
        if rec2[2] <= rec1[0]: 
            return False
        
        # above or below
        if rec1[1] >= rec2[3]:
            return False
        if rec2[1] >= rec1[3]:
            return False
        
        return True 
