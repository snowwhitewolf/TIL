from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
def bfs(sy, sx):
    global yy, xx
    visited = [[0] * w for _ in range(h)]
    queue = deque()
    queue.append([sy, sx])
    while queue:
        y, x = queue.popleft()
        if [y, x] in dust:
            dust.remove([y, x])
            yy = y
            xx = x
            return visited[y][x]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < w and 0 <= ny < h:
                if visited[ny][nx] == 0 and MAP[ny][nx] != 'x':
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny, nx])
    return -1
while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    dust = []
    res = 0
    MAP = [input().rstrip() for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if MAP[y][x] == '*':
                dust.append([y,x])
            elif MAP[y][x] == 'o':
                sy = y
                sx = x
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    yy = sy
    xx = sx
    while dust:
        total = bfs(yy, xx)
        if total == -1:
            res = 0
            print(total)
            break
        res += total
    if res:
        print(res)