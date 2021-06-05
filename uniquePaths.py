class Solution(object):
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == n == 1:
            return 1
        
        # initilize dynamic programming matrix to all 1s
        dp = [[1]*m]*n

        # start at 1 because first row and col will be 1s which are already set
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                # set current value to one above plus one to the left
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        # return bottom right index
        return dp[-1][-1]
