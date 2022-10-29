def lonelyinteger(a):
    # Write your code here
    freq = {}
    for num in a: 
        if num not in freq: 
            freq[num] = 1
        else: 
            freq[num] += 1
    
    for key, val in freq.items():
        if val == 1:
            return key
    
    return -1
            
