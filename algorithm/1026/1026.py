'''
1~M : 일반
-1 : 블랙
0 : 무지개

블록 그룹
일반 블록 적어도 1개
일반 블록 색깔 통일
검은색 블록 X
무지개 블록 상관 X
2개 이상
y,x 작은순

오토 플레이(블록이 있을때까지 반복)
1. 블록 크기 > 무지개 블록 수 > 기준 블럭 y,x 큰순
2. 블록 제거 점수 + 개수**2
3. 중력 작용(검은색 블록 제외)
4. 반시계 방향으로 회전
5. 중력 작용(검은색 블록 제외)
'''


import sys
sys.stdin = open('input.txt','r')

def find_block(y,x):
    global big_block
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if [ny, nx] in block:
            continue
        if MAP[ny][nx] == n or MAP[ny][nx] == 0:
            block.append([ny,nx])
            find_block(ny,nx)
    if len(block) >= len(big_block):
        big_block = block
    return

def delete(block):
    for i in range(len(block)):
        y = block[i][0]
        x = block[i][1]
        MAP[y][x] = -2
    return

N,M = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]
res = 0

while True:
##### 블럭 찾기
    big_block = []
    for y in range(N):
        for x in range(N):
            block = []
            block.append([y, x])
            n = MAP[y][x]
            find_block(y,x)

##### 블럭크기가 1이면 종료
    if len(big_block)==1:
        break
##### 블럭 삭제
    delete(big_block)
##### 점수 증가
    res += len(big_block)**2
##### 중력 작용
    for x in range(N):
        for y in range(N-1,-1,-1):
            pass

####### 반시계 방향 회전
    nMAP = [[0]*N for _ in range(N)]
    for _ in range(3):
        for y in range(N):
            for x in range(N):
                nMAP[y][x] = MAP[N-1-x][y]

        for y in range(N):
            for x in range(N):
                MAP[y][x] = nMAP[y][x]

##### 중력 작용
    for x in range(N):
        for y in range(N-1,-1,-1):
            pass

print(res)
