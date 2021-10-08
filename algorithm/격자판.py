import sys
sys.stdin = open("input.txt",'r')


def func(y, x, num):
    if len(num) == 7:
        if num not in res:
            res.append(num)
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny > 3 or nx < 0 or nx > 3:
            continue
        func(ny, nx, num + MAP[ny][nx])

for t in range(1,int(input())+1):
    MAP = [list(input().split()) for _ in range(4)]
    res = []
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    for y in range(4):
        for x in range(4):
            func(y,x,f'{MAP[y][x]}')
    print('#{} {}'.format(t,len(res)))


