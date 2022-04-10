from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    queue = deque()
    queue.append([y,x])
    visited = [[0]*(w+2) for _ in range(h+2)]
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < h+2 and 0 <= nx < w+2:
                if visited[ny][nx] == 0:
                    if MAP[ny][nx] == '.' or MAP[ny][nx] == '$':
                        visited[ny][nx] = visited[y][x]
                        queue.appendleft([ny,nx])
                    elif MAP[ny][nx] == '#':
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append([ny,nx])
                    else:
                        continue
    return visited


for t in range(int(input())):
    total = 1234567890
    P = []
    h, w = map(int,input().split())
    MAP = [list('.'*(w+2))]
    for _ in range(h):
        MAP.append(list('.'+input().rstrip()+'.'))
    MAP.append(list('.'*(w+2)))
    for y in range(h+2):
        for x in range(w+2):
            if MAP[y][x] == '$':
                P.append([y,x])

    first = bfs(P[0][0], P[0][1])
    second = bfs(P[1][0], P[1][1])
    third = bfs(0,0)

    # for i in range(len(first)):
    #     print(*first[i])
    # print()
    # for i in range(len(second)):
    #     print(*second[i])
    # print()
    # for i in range(len(third)):
    #     print(*third[i])
    
    # ny, nx = 0, 0
    # i = 0
    # while True:
    #     if i == 4:
    #         break
    #     ny += dy[i]
    #     nx += dx[i]
    #     if 0 <= ny < h and 0 <= nx < w:
    #         if first[ny][nx] and second[ny][nx]:
    #             res = first[ny][nx] + second[ny][nx] - 2
    #             total = min(total,res)
    #     else:
    #         ny -= dy[i]
    #         nx -= dx[i]
    #         i += 1

    for y in range(h+2):
        for x in range(w+2):
            if first[y][x] and second[y][x] and third[y][x]:
                res = first[y][x] + second[y][x] + third[y][x] - 3
                if MAP[y][x] == '#':
                    res -= 2
            total = min(total,res)
    print(total)
