from itertools import count
from operator import le
import os
import re
import sys

def solve(data):
    results = []
    data.sort()
    length = len(data)

    for i, a in enumerate(data):
        if i > 0 and a == data[i - 1]:
            continue
        left = i + 1
        right = length - 1
        while left < right:
            threeSum = a + data[left] + data[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                results.append([a, data[left], data[right]])
                while left < right and data[left] == data[left + 1]:
                    left += 1
                while left < right and data[right] == data[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data))