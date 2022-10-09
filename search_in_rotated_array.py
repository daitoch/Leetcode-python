from datetime import date
from operator import truediv
import os
from re import M
import sys

def solve(data, target) -> int:
    left, right  = 0 , len(data) - 1
    if len(data) is None:
        return "False"
    while left <= right:
        mid = (right + left) // 2
        if data[mid] == target:
            return "True"
      
        if data[left] <= data[mid]:
            if target > data[mid] or target < data[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < data[mid] or target > data[right]:
                right = mid - 1
            else:
                left = mid + 1

    return "False"
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data, target))