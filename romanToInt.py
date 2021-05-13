class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s is None:
            return 0
        
        value = 0
        sum = 0
        prev = 20000 # greater than max val
 
        for char in s:
            if char == "I":
                value = 1
            elif char == "V":
                value = 5
            elif char == "X":
                value = 10
            elif char == "L":
                value = 50
            elif char == "C":
                value = 100
            elif char == "D":
                value = 500
            elif char == "M":
                value = 1000
            else:
                print "Invalid value"
            
            if value > prev:
                # remove prev written value and next
                sum = sum - (prev*2)
                sum = sum + value
            else:
                sum = sum + value
            
            prev = value
        
        
        return sum
