class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        isFound = False
        
        # iterate the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtracking(board, word, i, j, 0, isFound)
                if isFound == True: 
                    break
        
        return isFound
    
    
    def backtracking(self, board, word, i, j, index, isFound):
        # direction
        if index == len(word)-1:
            isFound = True
            return
        if i > len(board) or j > len(board) or i < 0 or j < 0:
            return
    
        if board[i][j] == word[index]:
            board[i][j] = "0"
            index = index + 1
        
        
        self.backtracking(board, word, i+1, j, index, isFound) # to the right
        self.backtracking(board, word, i-1, j, index, isFound) # to the left
        self.backtracking(board, word, i, j+1, index, isFound) # go up
        self.backtracking(board, word, i, j-1, index, isFound) # go down
            
        return isFound
