from calendar import c
import os
import sys

def solve(data):
    result = [1] * (len(data))
    for i in range(len(data) -1, -1, -1):
        for j in range(i + 1, len(data)):
            if data[i] < data[j]:
                result[i] = max(result[i], 1 + result[j])
    return max(result)

    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))