import os, sys

def solve(data):
    res =[]
    
    data.sort(key = lambda i : i[0])
    res.append(data[0])
    for i in range(1, len(data)):
        if res[-1][1] < data[i][0]:
            res.append(data[i])
        elif res[-1][0] > data[i][1]:
            res.append[data[i]]
        else:
            min_res = res[-1][0]
            min_data =  data[i][0]
            max_res = res[-1][1]
            max_data = data[i][1]
            target = [min(min_res, min_data), max(max_res, max_data)]
            res[-1] = target
    
    return res
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = [[1,4],[0,4]]
    print(solve(data))