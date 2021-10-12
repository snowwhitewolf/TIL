import sys
sys.stdin = open('input.txt','r')


def drop(num):
    for i in range(H):
        if MAP[i][num]:
            boom(i, num, MAP[i][num] - 1)
            return


def boom(y, x, l):
    if l == 0:
        MAP[y][x] = 0
        return
    else:
        MAP[y][x] = 0
        for ll in range(l):
            for d in range(4):
                ny = y + dy[d] * l
                nx = x + dx[d] * l
                if 0 <= ny < H and 0 <= nx < W:
                    boom(ny, nx, MAP[ny][nx] - 1)
                    return

for t in range(int(input())):
    N,W,H = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(H)]
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    drop(2)
    for k in range(H):
        print(MAP[k])
    print()
    drop(2)
    for k in range(H):
        print(MAP[k])



