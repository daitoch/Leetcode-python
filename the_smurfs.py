import os, sys

def solve(data, target):
    r = b = g = 0
    for i in range(len(data)):
        if data[i] == "R": r += 1
        if data[i] == "B": b += 1
        if data[i] == "G": g += 1
    if r == len(data) or b == len(data) or g == len(data):
        return len(data)

    if (r%2==0 and b%2==0 and g%2==0) or (r%2==1 and b%2==1 and g%2==1):
        return 2
    else:
        return 1
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(str, input().strip().split(',')))
    print(solve(data, target))