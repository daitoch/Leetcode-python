import os, sys

def solve(data):
    data.sort(key = lambda i : i[0])

    res = True
    last = data[0][1]
    for start, end in data[1:]:
        if start >= last:
            last = end
        else:
            return False
            

    return True
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = [[0, 30], [5, 10], [15, 20]]
    print(solve(data))