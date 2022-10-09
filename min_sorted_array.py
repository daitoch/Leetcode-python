import os
import sys

def solve(data) -> int:
    low = high = data[0]

    for i in range(1, len(data)):
        if low <= data[i]:
            high= data[i]
        else:
            low = data[i]
    return low
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))