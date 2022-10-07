import os
from pickle import TRUE
import sys

def solve(data):
    prevMap = set() # hashmap for previous values

    for value in data:
        if value in prevMap:
            return "True"
        else:
            prevMap.add(value)
    return "False"

    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))