import os
import sys

def solve(data, target):
    dp = [target + 1] * (target + 1)
    dp[0] = 0
    for amount in range(1, target + 1):
        for coin in data:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    return dp[target] if dp[target] != target + 1 else -1
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data, target))