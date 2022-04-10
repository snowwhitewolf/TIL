import sys
sys.stdin = open('input.txt','r')

R, C, K = map(int,input().split())
MAP1 = [list(map(int,input().split())) for _ in range(R)]
W = int(input())
Wlst = [list(map(int,input().split())) for _ in range(W)]
res = 0
MAP = [[0]*C for _ in range(R)]
hot = []
ex = []
warm = [[0]*C for _ in range(R)]

def check(ex):
    for i in range(ex):
        if MAP[ex[i][0]][ex[i][1]] < K:
            return False
    return True

for y in range(R):
    for x in range(C):
        if 1 <= MAP1[y][x] <= 4:
            hot.append([y,x,MAP1[y][x]])
        elif MAP1[y][x] == 5:
            ex.append([y, x])

while True:
    for i in range(len(hot)):
        up = 5
        sy, sx = hot[i][0], hot[i][1]

        if hot[i][2] == 1:
            y, x = sy, sx + 1
            if 0 <= y <= R and 0 <= x <= C:
                warm[y][x] += up
                up -= 1
            else:
                break
            dd = 3
            while up != 0:
                y -= 1
                x += 1
                if x >= C:
                    break
                for d in range(dd):
                    dy, dx = y+d, x
                    if 0 <= dy < R and 0 <= dx < C:
                        warm[dy][dx] += up
                dd += 2
                up -= 1

        if hot[i][2] == 2:
            y, x = sy, sx - 1
            if 0 <= y <= R and 0 <= x <= C:
                warm[y][x] += up
                up -= 1
            else:
                break
            dd = 3
            while up != 0:
                y -= 1
                x -= 1
                if x < 0:
                    break
                for d in range(dd):
                    dy, dx = y+d, x
                    if 0 <= dy < R and 0 <= dx < C:
                        warm[dy][dx] += up
                dd += 2
                up -= 1

        if hot[i][2] == 3:
            y, x = sy - 1, sx
            if 0 <= y <= R and 0 <= x <= C:
                warm[y][x] += up
                up -= 1
            else:
                break
            dd = 3
            while up != 0:
                y -= 1
                x += 1
                if y < 0:
                    break
                for d in range(dd):
                    dy, dx = y, x-d
                    if 0 <= dy < R and 0 <= dx < C:
                        warm[dy][dx] += up
                dd += 2
                up -= 1

        if hot[i][2] == 4:
            y, x = sy + 1, sx
            if 0 <= y <= R and 0 <= x <= C:
                warm[y][x] += up
                up -= 1
            else:
                break
            dd = 3
            while up != 0:
                y += 1
                x -= 1
                if y >= R:
                    break
                for d in range(dd):
                    dy, dx = y, x + d
                    if 0 <= dy < R and 0 <= dx < C:
                        warm[dy][dx] += up
                dd += 2
                up -= 1

    for y in range(R):
        for x in range(C):
            MAP[y][x] += warm[y][x]


    for i in range(R):
        print(*MAP[i])
    print('---------------')
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    y,x = 0,0
    d = 0
    while d <= 3:
        if MAP[y][x] > 0:
            MAP[y][x] -= 1
        y += dy[d]
        x += dx[d]
        if y < 0 or y >= R or x < 0 or x >= C:
            y -= dy[d]
            x -= dx[d]
            d += 1
    for i in range(R):
        print(*MAP[i])
    break

    res += 1
    if res > 100:
        res = 101
        break
    if check(ex):
        break