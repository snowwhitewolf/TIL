for t in range(int(input())):
    n = int(input())
    maze = []
    for i in range(n):
        maze.append(input())
    visited = [[0 for _ in range(n)] for _ in range(n)]