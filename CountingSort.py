def countingSort(arr):
    # Write your code here
    freqArray = [0] * 100
    for item in arr: 
        freqArray[item] += 1
    
    return freqArray
