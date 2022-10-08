import os
import sys

def solve(data):
    # This is problem of dynamic programming.
    if data is None or len(data) == 0:
        return 0
    maxHere = minHere = maxSoFar= data[0]
    for i in range(1,len(data)):
        mx, mn = maxHere, minHere
        # This will take a record of both the maximum and minimum product
        # of the array 
        maxHere = max(max(mx * data[i], data[i]), mn*data[i])
        minHere = min(min(mn * data[i], data[i]), mx*data[i])
        maxSoFar = max(maxHere, maxSoFar)
    return maxSoFar
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))