class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        lefts  = []
        rights = []
        num_splits = 0
        
        for letter in s: 
            if letter == "R": 
                rights.append("R")
            if letter == "L": 
                lefts.append("L")
            if len(lefts) == len(rights): 
                num_splits += 1
                lefts = []
                rights = []
        
        return num_splits
            
