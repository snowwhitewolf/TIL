dy = [0,0,1,-1]
dx = [1,-1,0,0]


def f(y, x):
    MAP[y][x] = 0
    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and MAP[y + dy[i]][x + dx[i]]:
            f(y + dy[i], x + dx[i])
    return
for t in range(int(input())):
    M,N,K = map(int,input().split())
    MAP = [[0]*M for _ in range(N)]
    for i in range(K):
        x,y = map(int,input().split())
        MAP[y][x] = 1
    cnt = 0
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 1:
                cnt += 1
                f(y,x)
    print(cnt)