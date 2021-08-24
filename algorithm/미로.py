def dfs(y,x):
    global cnt
    if maze[y][x] == '1':
        return
    if visited[y][x] == 1:
        return
    if maze[y][x] == '3':
        cnt = 1
        return


    visited[y][x] = 1
    if 0<= x <= n-1 and 0<= y-1 <= n-1:
        dfs(y-1,x) #위
    if 0 <= x <= n - 1 and 0 <= y+1 <= n - 1:
        dfs(y+1,x) #아래
    if 0 <= x-1 <= n - 1 and 0 <= y <= n - 1:
        dfs(y,x-1) #왼쪽
    if 0 <= x+1 <= n - 1 and 0 <= y <= n - 1:
        dfs(y,x+1) #오른쪽
    return


for t in range(int(input())):
    n = int(input())
    maze = []
    for i in range(n):
        maze.append(input())
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    s_y = 0
    s_x = 0
    for y in range(n):
        for x in range(n):
            if maze[y][x] == '2':
                s_y = y
                s_x = x
    dfs(s_y,s_x)
    print('#{} {}'.format(t+1,cnt))