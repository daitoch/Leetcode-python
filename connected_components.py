import os, sys

def solve(data, target):
    parent = [i for i in range(target)]
    rank = [0 for i in range(target)]

    def find(node):
        if node == parent[node]:
            return node
        
        parent[node] = find(parent[node])
        return parent[node]
    
    def union(node1, node2):
        u = find(node1)
        v = find(node2)

        if u != v:
            if rank[u] < rank[v]:
                u, v = v, u

            parent[v] = u

            if rank[u] ==rank[v]:
                rank[u] = rank [v] + 1
    
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    target = int(input())
    data = list(map(int, input().split(' ')))
    print(solve(data, target))