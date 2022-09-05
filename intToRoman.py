class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret_string = ""
        num_digits = len(str(num))
        multiplier = 10
        
        while num > 0: 
            # thousands --------------------------
            if num_digits > 3:
                digit = int(num / 1000)
                ret_string += (digit * "M")
                num = num - (digit * 1000)
            
            # hundreds ---------------------------
            elif num_digits > 2:
                digit = int(num/100)
                if digit == 9: 
                    ret_string += "CM"
                    num = num - 900
                elif digit >= 5:
                    ret_string += "D"
                    num = num - 500
                elif digit == 4:
                    ret_string += "CD"
                    num = num - 400
                else:
                    ret_string += (digit * "C")
                    num = num - (digit *100)
            
            # tens ------------------------------------
            elif num_digits > 1: 
                digit = int(num/10)
                if digit == 9: 
                    ret_string += "XC"
                    num = num - 90
                elif digit >=5:
                    ret_string += "L"
                    num = num - 50
                elif digit == 4:
                    ret_string += "XL"
                    num = num - 40
                else: 
                    ret_string += ("X" * digit)
                    num = num - (10 * digit)
    
            # ones ------------------------------------
            else:
                if num == 9: 
                    ret_string += "IX"
                    num = 0
                elif num >= 5: 
                    ret_string += "V"
                    num = num -5
                elif num == 4: 
                    ret_string += "IV"
                    num = 0
                else: 
                    ret_string += (num * "I")
                    num = 0
                    
            
            num_digits = len(str(num))
        
        return ret_string
                

            
            
                
            
