import sys
import os

def solve(data, target):
    low = 0
    high = len(data) -1

    while low < high:
        sum = data[low] + data[high]
        if sum == target:
            print(low, high)
            return
        elif sum > target:
            high = high -1
        else:
            low = low + 1
    return

def solve_hashmap(data, target) -> list[int]:
    prevMap = {} # hash map to store the previous values
    for i,n in enumerate(data):
        diff = target - n
        if diff in prevMap:
            return[prevMap[diff], i]
        prevMap[n] = i
    return

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    #solve(data, target)
    print(solve_hashmap(data, target))