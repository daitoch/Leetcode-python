import os, sys

def solve(data):
    rob1, rob2 = 0, 0

    for i in data:
        rob1, rob2 = rob2, max(rob1 + i, rob2)

    return rob2
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))