import os, sys

def solve(data):
    data.sort()
    last = data[0][1]
    res = 0

    for start, end in data[1:]:
        if start >= last:
            last = end
        else:
            res += 1
            last = min(last, end)
    return res


    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(solve(data))