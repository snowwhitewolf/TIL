import copy
from collections import deque
import sys
sys.stdin = open("text.txt","r")

T = int(input())


def drop(x) :
    t = H-1# 떨어뜨릴 위치
    for y in range(H-1 , -1,-1):
        if MAP[y][x] != 0 :
            backup = MAP[y][x]
            MAP[y][x] = 0
            MAP[t][x] = backup
            t -=1
    return

def gravity():
    # 0 ~ W-1 다 떨어뜨리기
    for x in range(W) :
        drop(x)
    return

def go(x): # 연쇄 폭발
    # y 좌표 찾기
    for y in range(H):
        if MAP[y][x] > 0 :
            break
    visited = [[0] * W for _ in range(H)]
    qu = deque()
    visited[y][x] = 1
    qu.append((y,x,MAP[y][x])) # 좌표 / power
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while qu : # 폭발 예약이 걸려있는동안
        sy,sx ,power = qu.popleft()
        MAP[sy][sx] = 0 # 폭발됨
        for t in range(4) : # 방향 t
            i = 0
            ny, nx = sy, sx
            while i < power - 1 :
                ny += dy[t]
                nx += dx[t]
                if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == 0 and MAP[ny][nx] != 0 :
                    qu.append((ny,nx, MAP[ny][nx])) # 연쇄 폭발될 좌표들 등록
                i += 1
    return

def get_cnt(MAP):
    cnt = 0
    for y in range(H):
        for x in range(W) :
            if MAP[y][x] > 0 :
                cnt += 1
    return cnt


def dfs(level ,path) :
    global min_cnt, MAP
    if level == N :
        # 남은 벽돌을 카운트
        min_cnt = min(get_cnt(MAP), min_cnt)
        return

    backup = copy.deepcopy(MAP)
    for x in range(W) :
        go(x)# 연쇄폭발
        gravity() # 중력 작용
        path.append(x)
        dfs(level + 1, path)
        path.pop()
        MAP = copy.deepcopy(backup)# 원상복구

for tc in range(1, T+ 1) :
    N, H, W = map(int ,input().split())
    MAP = [
        list(map(int ,input().split())) for _ in range(H)
    ]
    path = []
    min_cnt = int(21e8)
    dfs(0, path)
    print("#{} {}".format(tc, min_cnt))