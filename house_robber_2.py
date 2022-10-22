import os, sys
import re

def solve(data):
    maxValue =  max(house_robber(data[1:]), house_robber(data[:-1]))
    return maxValue
    pass

def house_robber(data):
    rob1, rob2 = 0, 0
    for i in data:
        rob1, rob2 = rob2, max(i+rob1, rob2)
    return rob2

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))