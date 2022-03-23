import sys
sys.stdin = open("input.txt",'r')
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,1,-1]
Y,X = map(int,input().split())
MAP = []
for i in range(Y):
    MAP.append(input())
print(MAP)
def bfs(y,x):
    Q = deque
    Q.append(y,x)
    visited = [[0]*X for _ in range(Y)]
    while Q:
        sty,stx = Q.popleft()
        for i in range(4):
            if 0<= sty+dy[i] <=Y and 0<= stx+dx[i] <=X and visited[sty+dy[i]][stx+dx[i]] == 0:
                visited[sty+dy[i]][stx+ dx[i]] = visited[sty][stx] + 1
                sty = sty + dy[i]
                stx = stx + dx[i]
                Q.append(sty,stx)
    return

for y1 in range(Y):
    for x1 in range(X):
        if MAP[y1][x1] == 'L':
            bfs(y1,x1)
            de = -1