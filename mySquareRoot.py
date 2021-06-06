class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        start = 1
        end = x
        
        while start <= end: 
            # get mid point
            mid = (start + end )//2
            
            # get squared value
            mid_sq = mid * mid
            
            if mid_sq == x: 
                return mid
            
            # if squared val is less than x search in right half
            if mid_sq < x: 
                start = mid + 1
                answer = mid
            # if squared val is greater than x search in left half
            else:
                end = mid - 1
        
        return answer
