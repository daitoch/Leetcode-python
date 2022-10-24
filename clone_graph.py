import os, sys

class Node:
    def __init__(self, value = 0, neighbour = None):
        self.value = value
        self.neighbour = neighbour
        pass

def solve(node):
    hashMap = {}

    def dfs(node):

        if node in hashMap:
            return hashMap[node]

        copy = Node(node.value)
        hashMap[node] = copy

        for n in node.neighbour:
            copy.neighbour.append(dfs(n))

        return copy


    return dfs(node) if node else None
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data, target))