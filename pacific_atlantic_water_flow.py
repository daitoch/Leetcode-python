import os, sys

def solve(heights):
    ROWS, COL = len(heights), len(heights[0])

    pac, atl = set(), set()
    def dfs(r, c, visited, prevHeight):
        if (r < 0 or c < 0 or r == ROWS or c == COL or(r, c) in visited or heights[r][c] < prevHeight):
            return
        visited.add(r, c)
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COL -1, atl, heights[r][COL-1])

    for c in range(COL):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS -1, c, atl, heights[ROWS -1][c])

    res = []
    for r in range(ROWS):
        for c in range(COL):
            if (r,c) in pac and (r,c) in atl:
                res.append([r,c])
    return res

    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data, target))