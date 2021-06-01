class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        isFound = False
        if not board:
            return isFound
        
        # iterate the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                isFound = self.backtracking(board, word, i, j)
                if isFound == True: 
                    return isFound
        
        return isFound
    
    
    def backtracking(self, board, word, i, j):
        # found whole word
        if len(word) == 0:
            return True
        
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or word[0] != board[i][j]:
            return False
        
        # Save value at index
        temp = board[i][j]
        
        # set value to visited
        board[i][j] = "#"
        
        # check in four directions
        right = self.backtracking(board, word[1:], i+1, j) # to the right
        left = self.backtracking(board, word[1:], i-1, j) # to the left
        up = self.backtracking(board, word[1:], i, j+1) # go up
        down = self.backtracking(board, word[1:], i, j-1) # go down
        
        # reset value
        board[i][j] = temp
        
        return (right or left or up or down)
