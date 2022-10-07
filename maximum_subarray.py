import os
import sys

def solve(data):
    maxEnding = maxSoFar = data[0]

    for i in range(1, len(data)):
        maxEnding = max(maxEnding + data[i], data[i])
        maxSoFar = max (maxEnding, maxSoFar)
    return maxSoFar
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data)) 