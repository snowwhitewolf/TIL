from collections import deque
dy = [0,0,1,-1]
dx = [1,-1,0,0]
def bfs(y,x):
    qu = deque()
    #시작점
    qu.append((y,x))
    visited[y][x] = 1
    #bfs시작
    while qu:
        y,x = qu.popleft()

        for t in range(4):
            ny = y +dy[t]
            nx = x+ dx[t]
            if ny < 0 or nx < 0 or ny >= n or nx >=m:
                continue
            if lst[ny][nx] == 0:
                continue
            if visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            qu.append((ny, nx))

for t in range(int(input())):
    n,m = map(int,input().split())
    lst = list()
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    cnt = 0
    visited = [[0] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if lst[y][x] == 2 and visited[y][x] == 0:
                bfs(y, x)
                cnt += 1
    print('#{} {}'.format(t+1, cnt))