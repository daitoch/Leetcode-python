import os, sys

def solve(data, target):
    res = []

    for i in range(len(data)):

        if target[1] < data[i][0]:
            res.append(target)
            return res + data[i:]
        elif target[0] > data[i][1]:
            res.append(data[i])
        else:
            target = [min(target[0], data[i][0]), max(target[1], data[i][1])]
    
    res.append(target)
    return res
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = [4, 8]
    data = [[1,2],[3,5],[6,7],[8,10],[12,16]]

    print(solve(data, target))