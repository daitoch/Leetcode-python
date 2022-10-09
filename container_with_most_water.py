import os
import sys

def solve(data):
    left, right = 0, len(data) - 1
    result = 0
    while left < right:
        area = (right - left) * min(data[left], data[right])
        result = max (area, result)
        if data[left] < data[right]:
            left += 1
        elif data[left] < data[right]: 
            right -= 1
        else:
            right -= 1

    return result
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))