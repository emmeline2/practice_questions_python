class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dividendIsNegative = False
        divisorIsNegative = False
        
        # handle negatives
        if dividend < 0:
            dividendIsNegative = True
            dividend = dividend * (-1)
        if divisor < 0:
            divisorIsNegative = True
            divisor = divisor * (-1)
        
        # Compute result
        result = dividend / divisor
        
        # convert to int
        int_result = int(result)
        
        # handle overflows
        if int_result > ((2 ** 31) - 1):
            int_result = ((2 ** 31) - 1)
            if (dividendIsNegative and not divisorIsNegative) or (not dividendIsNegative and divisorIsNegative):
                int_result = int_result + 1
        
        if (dividendIsNegative and divisorIsNegative) or (not dividendIsNegative and not divisorIsNegative):
                return int_result
        else:
            return int_result * -1
