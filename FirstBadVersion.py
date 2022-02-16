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
        
        for item in range(1, n): 
            if isBadVersion(item): 
                return item
        
        # catch the case of last item is bad
        return n
