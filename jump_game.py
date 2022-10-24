import os, sys

def solve(data):
    high = len(data) - 1
    for i in range(len(data) - 1, -1 ,-1):
        if i + data[i] >= high:
            high = i
    return True if high == 0 else False
        
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))