class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        # compute the sqaures each time
        # keep track of past results
        # if go in a cycle (repeat value) return false
        # if get to 1 eventually return true 

        record = set() # sets do not allow duplicates
        while (n!=1) and (n not in record):
            record.add(n)
            n = sum(int(i)**2 for i in str(n))
        return (n==1)
