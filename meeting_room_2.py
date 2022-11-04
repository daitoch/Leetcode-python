import os, sys

def solve(data):
    data.sort(key = lambda i : i[0])
    last = data[0][1]
    rooms = 0
    for start, end in data[1:]:
        if start >= last:
            # This means that these are non overlapping meetings
            last = end
        else:
            # For overlapping meeting add a room
            rooms += 1
    return rooms
    pass

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    #target = int(input())
    data = [[0, 30], [15, 20], [5, 10]]
    print(solve(data))