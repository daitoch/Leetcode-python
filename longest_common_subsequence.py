import os
import sys


def solve(data, target):
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data, target))