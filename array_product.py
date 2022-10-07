import os
import sys
from turtle import pos

def solve(data):
    output = [1] * len(data)
    prefix, postfix = 1, 1
    length = len(data)
    j = length - 1
    for i in range(length):
        output[i] = prefix
        prefix *= data[i]

    while j >= 0:
        output[j] *= postfix
        postfix *= data[j]
        j -=1

    return output
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))