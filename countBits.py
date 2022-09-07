class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(0,n+1):
            ones = 0
            binary = bin(i).replace("0b", "")
            for char in binary:
                if char == '1': 
                    ones += 1
            result.append(ones)
            
        
        return result
            
