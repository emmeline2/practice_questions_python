#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # At each index in the left upper quadrent each index can be one of the four values, find the max of those four values
    
    t = len(matrix) - 1
    half = len(matrix) // 2
    maxSum = 0
    
    for i in range(half):
        for j in range(half):
            # find max of the four values 
            maxValue = max(matrix[i][j], matrix[i][t - j], \
                matrix[t-i][j], matrix[t-i][t-j])
            maxSum += maxValue
    
    return maxSum
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
