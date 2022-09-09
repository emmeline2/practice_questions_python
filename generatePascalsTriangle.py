class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        output = []
        
        for i in range(0, numRows):
            row_array = []
            for j in range(0,i+1):
                # add 1 if in first or last index in a row
                if (j == 0) or (j == i): 
                    row_array.append(1)
                else:
                    # fill with sum of two elements above
                    temp = output[i - 1][j] + output[i - 1][j - 1]
                    row_array.append(temp)
            # add row to output list
            output.append(row_array)
        
        return output
                
