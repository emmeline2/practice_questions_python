def miniMaxSum(arr):
    # Write your code here
    totalSum = sum(arr)
    maxVal = max(arr)
    minVal = min(arr)
    
    minimum = totalSum - maxVal
    maximum = totalSum - minVal
    
    print(str(minimum) + " " + str(maximum))
