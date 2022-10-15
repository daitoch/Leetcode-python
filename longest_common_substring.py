import sys, os

def solve(data, target):
    if len(data) == 0 or len(target) == 0:
        return 0
    d_len, t_len = len(data) - 1, len(target) -1
    if data[d_len] == target[t_len]:
        return 1 + solve(data[:-1], target[:-1])
    else:
        return max(solve(data,target[:-1]), solve(data[:-1], target))
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = str(input())
    data = str(input())
    print(solve(data, target))