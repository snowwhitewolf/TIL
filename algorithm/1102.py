import sys
sys.stdin = open('input.txt','r')

N,M,K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(N)]
MAP = [list([] for _ in range(N)) for _ in range(N)]
A = [[5]*N for _ in range(N)]
DEAD = [[0]*N for _ in range(N)]
for i in range(M):
    x,y,z = map(int,input().split())
    MAP[y-1][x-1].append(z)
dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,1,-1,-1,0,1]
for _ in range(K):
    #봄
    for y in range(N):
        for x in range(N):
            MAP[y][x].sort()
            for n in range(len(MAP[y][x])):
                if MAP[y][x][n] <= A[y][x]:
                    A[y][x] -= MAP[y][x][n]
                    MAP[y][x][n] += 1
                # 여름 준비
                else:
                    DEAD[y][x] += MAP[y][x][n]//2
                    MAP[y][x][n] = 0
            while 0 in MAP[y][x]:
                MAP[y][x].remove(0)
    #여름
    for y in range(N):
        for x in range(N):
            A[y][x] += DEAD[y][x]
    #가을
    for y in range(N):
        for x in range(N):
            for n in range(len(MAP[y][x])):
                if MAP[y][x][n]%5==0:
                    for d in range(8):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0<= ny < N and 0<= nx < N:
                            MAP[ny][nx].append(1)
    #겨울
    for y in range(N):
        for x in range(N):
            A[y][x] += B[y][x]

res = 0
for y in range(N):
    for x in range(N):
            res += len(MAP[y][x])
print(res)