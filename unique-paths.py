import os, sys
from tkinter import N

def solve(left, right):
    row = [1] * right
    for i in range(left - 1):
        newRow = [1] * right
        for j in range(right - 2, -1, -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow

    return row[0]

    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = int(input())
    #data = list(map(int, input().split(' ')))
    print(solve(data, target))