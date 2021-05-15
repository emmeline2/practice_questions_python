class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix[0])
        
        print "Range: ", range(n // 2 + n % 2)
        
        for i in range(n // 2 + n % 2):
            # // = floor division: divide result is whole num rounded down
            for j in range( n// 2): 
                # swap index on four sides
                temp = matrix[n -1 -j][i] 
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
