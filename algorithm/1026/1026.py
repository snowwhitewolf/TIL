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
    global big_block, max_rain, rain
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if [ny, nx] in block:
            continue
        if MAP[ny][nx] == n or MAP[ny][nx] == 0:
            if MAP[ny][nx] == 0:
                rain += 1
            block.append([ny,nx])
            find_block(ny,nx)
    if len(block) >= len(big_block):
        if len(block) == len(big_block):
            if rain > max_rain:
                max_rain = rain
                big_block = block
        big_block = block
    return

def gravity(MAP):
    for y in range(N-2, -1, -1):
        for x in range(N):
            if MAP[y][x] > -1:
                r = y
                while True:
                    if 0<=r+1<N and MAP[r+1][x] == -2:
                        MAP[r+1][x] = MAP[r][x]
                        MAP[r][x] = -2
                        r += 1
                    else:
                        break

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

def turn():
    chg_MAP = []
    for x in range(N-1, -1, -1):
        new_line = []
        for y in range(N):
            new_line.append(MAP[y][x])
        chg_MAP.append(new_line)
    return chg_MAP

while True:
##### 블럭 찾기
    big_block = []
    max_rain = 0
    for y in range(N):
        for x in range(N):
            n = MAP[y][x]
            if n <= 0:
                continue
            if [y,x] in big_block:
                continue
            rain = 0
            block = []
            block.append([y, x])
            find_block(y,x)

##### 블럭크기가 1이면 종료
    if len(big_block)< 2:
        break

##### 블럭 삭제
    delete(big_block)

##### 점수 증가
    res += len(big_block)**2
##### 중력 작용
    gravity(MAP)

    MAP = turn()
##### 중력 작용
    gravity(MAP)
    print(res)
print(res)
