import os
import sys

def solve(data):
    #We .will use two pointer algo for this problem
    maxProfit, low = 0, data[0]
    for price in data:
        if low > price:
            low = price
        else:
            temp = price - low
            if temp > maxProfit:
                maxProfit = temp
    return maxProfit

    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))