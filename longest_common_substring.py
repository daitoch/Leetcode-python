from random import randrange
import sys, os

def solve_dp(data, target):
    # Solving the problem by saving all the answers in a
    # grid and hence utilizing DP paradgim
    DP_grid  = [[0 for i in range(len(target) + 1)] for j in range(len(data) + 1)]
    for i in range(len(data) - 1, -1, -1):
        for j in range(len(target) -1, -1, -1):
            if data[i] == target[j]:
                DP_grid[i][j] = 1 + DP_grid[i+1][j+1]
            else:
                DP_grid[i][j] = max(DP_grid[i][j+1], DP_grid[i+1][j])
    return DP_grid[0][0]

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
    print(solve_dp(data, target))
    print(solve(data, target))