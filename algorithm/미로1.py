def dfs(y, x):
    global cnt
    if maze[y][x] == 1:
        return
    if visited[y][x] == 1:
        return
    if maze[y][x] == 3:
        cnt = 1
        return
    visited[y][x] = 1
    dfs(y - 1, x)
    dfs(y + 1, x)
    dfs(y, x - 1)
    dfs(y, x + 1)
    return

for t in range(10):
    n = 0
    cnt = 0
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for y in range(16):
        if n == 1:
            break
        for x in range(16):
            if maze[y][x] == 2:
                n = 1
                dfs(y,x)
                break
    print('#{} {}'.format(tc,cnt))