class Solution(object):
# climb stairs, with options for stepping up one step or stepping up 2 steps

# when passed in the nubmer of steps, n determine the number of ways there are to climb the n stairs
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        list = []

        # base cases for 0 and 1
        list.insert(0, 1); 
        list.insert(1, 1); 
        
        # return if n is 0 or 1 
        if n is 0 or n is 1:
            return 1;
        
        # compute remaining sums up to n
        for i in range(2, n+1):
            list.insert(i, (list[i-1] + list[i-2]))
        
        return list[n]
