# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: 
            return 1
        if n == None: 
            return None
        
        left = 1
        right = n
        
        while left <= right:
            # get pivot value
            pivot = left + (right - left) // 2
            if isBadVersion(pivot): 
                right = pivot -1 
            else:
                left = pivot + 1
        
        return left
            
            
