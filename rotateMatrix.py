class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        # transpose the matrix, flip along the diagonal
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp

    
    def reflect(self, matrix):
        # reverse order in row
        n = len(matrix)
        for i in range(n): 
            # // = floor division: divide and round down to nearest whole num
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][-j-1]
                matrix[i][-j -1] = matrix[i][j]
                matrix[i][-j-1] = temp
                
