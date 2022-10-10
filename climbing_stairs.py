import os
import sys

def solve(n):
    d = [1] * 2
    for i in range(2, n+1):
        d[1], d[0] = d[1] + d[0], d[1]
    return d[1]
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    #data = list(map(int, input().split(' ')))
    print(solve(target))