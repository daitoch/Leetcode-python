from operator import le, truediv
import os, sys
import re
from tkinter import W

def solve(data: str, target) -> bool:
    dp_array = [False] * (len(target) + 1)
    dp_array[len(target)] = True

    for i in range(len(target) - 1, -1, -1):
        for w in data:
            if i+len(w) <= len(target) and target[i:i+len(w)] == w:
                dp_array[i] = dp_array[i+len(w)]
            if dp_array[i]:
                break
    return dp_array[0]
    

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = str(input())
    data = list(map(str, input().split(' ')))
    print(solve(data, target))