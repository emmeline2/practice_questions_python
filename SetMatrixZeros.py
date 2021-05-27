class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                    is_col = True
            for column in range(1, len(matrix[0])):
                if matrix[row][column] == 0:
                    matrix[row][0]= 0
                    matrix[0][column] = 0
        
        # Skip first column and row
        for i in range(1, len(matrix)):
            for j in range (1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
                
        # handle 1st row 
        if matrix[0][0] == 0: 
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        # handle 1st column
        if is_col: 
            for i in range(len(matrix)):
                matrix[i][0] = 0
                                    
        
