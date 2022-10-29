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
    # Write your code here
    currSum = 0
    half = int(len(matrix)/2)
    
    currSum = calculateSum(matrix, 0, 0)
    maxSum = currSum
    
    rowArry = []
    for row in range(0, half):
        rowArry = matrix[row][:]
        print("rowArray: ", rowArry)
        if sum(rowArry[0:half]) > sum(rowArry[half:]):
            matrix[row] = rowArry.reverse()
    
    colArry = []
    for col in range(0, half):
        colArry = matrix[:][col]
        if sum(colArry[0:half]) > sum(colArry[half:]):
            matrix[:][col] = colArry.reverse()
    
            
    currSum = calculateSum(matrix, 0, 0)
    maxSum = max(maxSum, currSum)
    return maxSum
            
def calculateSum(matrix, rowStart, colStart):
    currSum = 0
    quadrentLength = int(len(matrix)/2) -1
    print("length: ", len(matrix))
    print("Quadrent length: ", quadrentLength)
    print("rowStart", rowStart)
    print("colStart", colStart)
    for i in range(int(rowStart), int(rowStart+quadrentLength)):
        for j in range(int(colStart), int(colStart+quadrentLength)):
            currSum += matrix[i][j]
    
            return currSum
    
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
