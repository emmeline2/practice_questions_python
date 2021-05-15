
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove white space
        s = s.strip()

        # Check for empty
        if not s:
            return 0
        
        # Remove sign
        negative = False
        if s[0] == "-":
            negative = True
            # remove negative
            s = s[1:]
        elif s[0] == "+":
            # remove positive
            s = s[1:]
            
        # Remove leading zeros
        s.lstrip('0')
        
        # Check for empty again
        if not s:
            return 0
        
        # leading workds
        if s[0].isnumeric() is False:
            return 0
        if s.isnumeric() is False:
            # split on anythin not a digit
            temp = re.split(r'\D+',s)
            s = temp[0]
            
        # Convert to number
        num = int(s)
        
        # Handle nuegative
        if negative:
            num = num * -1
        
        # Check bounds condtions
        if num < -2147483648:
            num = -2147483648
        elif num > (2147483648 - 1):
            num = (2147483648 - 1)
        
        return num
