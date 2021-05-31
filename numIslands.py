class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        num_islands = 0
        
        # traverse the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': 
                    num_islands = num_islands + self.dfs(grid, i, j)
        
        return num_islands
    
    def dfs(self, grid, i, j):
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])): 
            return 0;
        if grid[i][j] != '1':
            return 0
        
        # sink the piece of island
        grid[i][j] = 0
        
        # check if land in four directions
        self.dfs(grid, i+1, j) # down
        self.dfs(grid, i-1, j) # up
        self.dfs(grid, i, j+1) # right
        self.dfs(grid, i, j-1) # down
        
        # return 1 to increment the num_islands count for found island
        return 1
