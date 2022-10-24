import os, sys

def solve(data, prereq):
    preMap = {i:[] for i in range(data)}

    for csr, pre in prereq:
        preMap[csr].append(pre)

    visited = set()

    def dfs(csr):
        if csr in visited:
            return False
        if preMap[csr] == []:
            return True

        visited.add(csr)

        for pre in preMap[csr]:
            if not dfs(pre): return False
        visited.remove(csr)
        preMap[csr] = []
        return True

    for csr in range(data):
        if not dfs(csr): return False
    return True
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    f = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    #data = list(map(int, input().split(' ')))
    print(f)
    print(solve(target,f))