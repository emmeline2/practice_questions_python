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
    # at each index in left upper quadrent each index can be one of four values
    # find the max of those four values
    t = len(matrix) - 1
    n = len(matrix) // 2
    max_sum = 0
    for i in range(n):
        for j in range(n):
            # find max of the four possible values
            max_value = max(matrix[i][j], \
            matrix[i][t - j], matrix[t-i][j], matrix[t-i][t-j])
            max_sum += max_value
    return max_sum

    
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
