import os, sys

def solve(data):
    dp = {len(data): 1}

    def decode(i):
        if i in dp:
            return dp[i]
        if data[i] == '0':
            return 0
        res = decode(i + 1)

        if i + 1 <len(data) and (int(data[i]) / 26 <= 1):
            res += decode(i+2)
        dp[i] = res
        return res
    return decode(0)
     


    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = str(input())
    #data = list(map(int, input().split(' ')))
    print(solve(target))