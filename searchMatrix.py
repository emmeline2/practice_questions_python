class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        
        # start at bottom left index
        y = m-1
        x = 0
        while x < n and y >= 0:
            if matrix[y][x] == target:
                return True
            # if value is less than target move to the right one column
            elif matrix[y][x] < target:
                x += 1
            # if value is greater than target move up one row
            else:
                y -= 1
        return False
