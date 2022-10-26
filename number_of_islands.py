import collections
import os, sys

def dfs(row, col, grid):
    grid[row][col] = "0"
    directions = [(row -1 , col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r,c in directions:
        if r in range(len(grid)) and c in range(len(grid[r])) and grid[r][c] == 1:
            dfs(r, c, grid)
    pass

    


def solve(data):
    island = 0
    visited = set()
    def bfs(row, col, grid):
        queue = collections.deque()
        visited.add((row, col))
        queue.append((row, col))
        while queue:
            row, col = queue.popleft()
            directions = [(row -1 , col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for r, c in directions:
                if r in range(len(data)) and c in range(len(data[r])) and data[r][c] == 1:
                    queue.append((r,c))
                    visited.add((r,c))


        pass
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 1:
                dfs(row, col, data)
                #bfs(row, col, data)
                island += 1
    return island
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = list(map(int, input().split(' ')))
    graph = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
    print(solve(graph))