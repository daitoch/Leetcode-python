import os, sys

def solve(data, target):
    res = []

    for i in range(len(data)):

        if target[1] < data[i][0]:
            res.append(target)
            return res + data[i:]
        elif target[0] > data[i][1]:
            res.append(target)
        else:
            target = [min(target[0], data[i][0]), max(target[1], data[i][1])]
    
    res.append(target)
    return res
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = [2, 5]
    data = [[1, 3], [6, 9]]
    print(solve(data, target))