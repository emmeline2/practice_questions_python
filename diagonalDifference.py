def diagonalDifference(arr):
    # Write your code here
    leftStartSum = 0
    rightStartSum = 0
    lColIndex = 0
    rColIndex = len(arr) - 1
    
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if lColIndex == j:
                leftStartSum += arr[i][j]
            if rColIndex == j: 
                rightStartSum += arr[i][j]
        lColIndex += 1
        rColIndex -= 1
    
    diagDifference = abs(leftStartSum - rightStartSum)
    
    return diagDifference
