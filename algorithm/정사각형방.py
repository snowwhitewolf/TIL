import sys
sys.stdin = open("input.txt",'r')

def func(idx,y, x, num):
    global cnt
    global start
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx]-MAP[y][x] == 1:
            if cnt <= num+1:
                if cnt == num+1:
                    start = min(start,idx)
                else:
                    start = idx
                cnt = num + 1
            func(idx,ny, nx, num + 1)


for t in range(1,int(input())+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    start = 0
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    for y in range(N):
        for x in range(N):
            func(MAP[y][x],y,x,1)

    print('#{} {} {}'.format(t,start,cnt))