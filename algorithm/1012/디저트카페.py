import sys
sys.stdin = open("../1019/input.txt", 'r')

dirs = [[-1, 1],[1, 1],[1, -1],[-1, -1]]

def dfs(sy, sx, dir, score, check):
    global res
    if 0 <= sy < N and 0 <= sx < N:
        if check >= 1 and dir >= 1:
            return

        if score > 0 and sy == y and sx == x:
            if res < score:
                res = score
            return

        if dir == 3 and len(des.keys()) * 2 <= res:
            return

        if des.get(MAP[sy][sx]):
            return

        des[MAP[sy][sx]] = 1

        dfs(sy+dirs[dir][0], sx+dirs[dir][1], dir, score+1, check)

        if check == 0:
            check = (dir+1)//4
        dfs(sy+dirs[(dir+1)%4][0], sx+dirs[(dir+1)%4][1], (dir+1)%4, score+1, check)
        del des[MAP[sy][sx]]


for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    res = -1

    for y in range(N):
        for x in range(N):
            des = {}
            dfs(y, x, 0, 0, 0)

    print('#{} {}'.format(t+1,res))