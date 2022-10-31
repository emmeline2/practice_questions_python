def gridChallenge(grid):
    
    # Write your code here
    for index in range(0, len(grid)):
        lineList = list(grid[index])
        lineList.sort()
        strLine = "".join(lineList)
        grid[index] = strLine
    
    matrix = []
    for index in range(0, len(grid)):
        lineList = list(grid[index])
        lineList.sort()
        matrix.append(lineList)
    
    for col in range(0, len(matrix[0])):
        column = [row[col] for row in matrix]
        sortedColumn = list(column)
        sortedColumn.sort()
        if column != sortedColumn:
            return "NO"
    
    return "YES"
    
