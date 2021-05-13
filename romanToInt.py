class Solution(object):
    roman_nums = {"I": 1, 
                  "V": 5, 
                  "X": 10,
                  "L": 50,
                  "C": 100, 
                  "D": 500,
                  "M": 1000}
    
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
            value = self.roman_nums.get(char)
            
            if value > prev:
                # remove prev written value and next
                sum = sum - (prev*2)
                sum = sum + value
            else:
                sum = sum + value
            
            prev = value
        
        return sum
