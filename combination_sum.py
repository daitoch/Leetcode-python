import os, sys
import re

def solve(data, target):
    res = []
    data.sort()

    def dfs(target, index, path):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        # Using a window which move forward and discard the previous number to 
        # This will remove duplicates from coming up
        # Essential once a number is checked for all the combinations it wont 
        # be checked again.
        for i in range(index, len(data)):
            dfs(target - data[i], i, path+[data[i]])
    dfs(target, 0, [])

    return res
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data, target))