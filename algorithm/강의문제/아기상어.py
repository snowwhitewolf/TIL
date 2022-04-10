import sys
sys.stdin = open('input.txt',"r")
from collections import deque

N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int,input().split())))
dy = [-1,0,1,0]
dx = [0,-1,0,1]
y1 =0
x1 = 0
res = 0
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 9:
            y1 = y
            x1 = x
            break
MAP[y1][x1] = 0
baby = 2
eat = []
up = 0

while True:
    q = deque()
    q.append((y1, x1, 0))
    visited = [[0] * N for _ in range(N)]
    while q:
        y, x, count = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if MAP[ny][nx] > baby or visited[ny][nx]:
                continue
            if 0 < MAP[nx][ny] < baby:
                eat.append((ny, nx, count + 1))
            visited[nx][ny] = 1
            q.append((ny, nx, count + 1))

    if eat:
        eat.sort()
        y = eat[0][0]
        x = eat[0][1]
        move = eat[0][2]
        res += move
        MAP[y][x] = 0
        up += 1
        if up == baby:
            baby +=1
            up = 0
        y1,x1 = y,x
    else:
        break
print(res)
