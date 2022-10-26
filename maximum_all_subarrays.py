import os, sys

def solve(arr,n, k):
    for i in range(n):
        if arr[i:k+i] is not None and k + i <= len(arr):
            res = (max(arr[i:k+i]))
            print(res)
    return
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    target_2 = 9
    data = list(map(int, input().split(' ')))
    print(solve(data, target_2, target))