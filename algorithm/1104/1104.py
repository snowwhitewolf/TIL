R,C,T = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(R)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
LG1 = 0
res = 2
for y in range(R):
    if MAP[y][0] == -1:
        LG1 = y
        break
LG2 = LG1 + 1
for _ in range(T):
    # 확산
    sMAP = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if MAP[y][x] > 4:
                cnt = 0
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0<=ny<R and 0<=nx<C and MAP[ny][nx]!=-1:
                        sMAP[ny][nx] += MAP[y][x]//5
                        cnt += 1
                MAP[y][x] -= (MAP[y][x]//5)*cnt
    # 확산 추가
    for y in range(R):
        for x in range(C):
            MAP[y][x] += sMAP[y][x]
    # 공기 청정기
    # 왼쪽
    for y in range(LG1-1,0,-1):
        MAP[y][0] = MAP[y-1][0]
    for y in range(LG2+1,R-1):
        MAP[y][0] = MAP[y+1][0]
    # 위쪽
    for x in range(C-1):
        MAP[0][x] = MAP[0][x+1]
        MAP[R-1][x] = MAP[R-1][x+1]
    # 오른쪽
    for y in range(0,LG1):
        MAP[y][C-1] = MAP[y+1][C-1]
    for y in range(R-1,LG2,-1):
        MAP[y][C-1] = MAP[y-1][C-1]
    # 아래쪽
    for x in range(C-1,1,-1):
        MAP[LG1][x] = MAP[LG1][x-1]
        MAP[LG2][x] = MAP[LG2][x-1]
    MAP[LG1][1] = 0
    MAP[LG2][1] = 0

for y in range(R):
        res += sum(MAP[y])
print(res)