import sys
sys.stdin = open('../1025/input.txt', 'r')

def first(man):
    total = []
    first_MAP = [[0]*N for _ in range(N)]
    max_cnt=0
    for y in range(N):
        for x in range(N):
            if MAP[y][x]:
                continue
            cnt = 0
            for d in range(4):
                bfy = y + dy[d]
                bfx = x + dx[d]
                if 0 <= bfy < N and 0 <= bfx < N:
                    if MAP[bfy][bfx] in like[f'{man}']:
                        cnt += 1
            max_cnt = max(cnt,max_cnt)
            first_MAP[y][x] = cnt
    for y in range(N):
        for x in range(N):
            if first_MAP[y][x] == max_cnt and MAP[y][x]==0:
                total.append([y,x])
    return total

def second(lst):
    if len(lst) == 1:
        return lst
    second_MAP = []
    max_cnt = 0
    for i in range(len(lst)):
        y = lst[i][0]
        x = lst[i][1]
        cnt = 0
        for d in range(4):
            bfy = y + dy[d]
            bfx = x + dx[d]
            if 0 <= bfy < N and 0 <= bfx < N:
                if MAP[bfy][bfx]==0:
                    cnt += 1
        max_cnt = max(cnt, max_cnt)
        lst[i].append(cnt)
    for i in range(len(lst)):
        if lst[i][2] == max_cnt and MAP[lst[i][0]][lst[i][1]]==0:
            second_MAP.append(lst[i][0:2])
            return second_MAP


N = int(input())
like = {}
lst = []
MAP = [[0]*N for _ in range(N)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
res = 0
for _ in range(N*N):
    a = list(map(int,input().split()))
    lst.append(a[0])
    like[f'{a[0]}'] = a[1:]
MAP[1][1] = lst[0]
for man in lst[1:]:
    p = second(first(man))
    y = p[0][0]
    x = p[0][1]
    MAP[y][x] = man
for y in range(N):
    for x in range(N):
        cnt = 0
        for d in range(4):
            bfy = y+dy[d]
            bfx = x+dx[d]
            if 0<= bfy < N and 0<= bfx < N:
                if MAP[bfy][bfx] in like[f'{MAP[y][x]}']:
                    cnt += 1
        if cnt != 0:
            res += 10**(cnt-1)
print(res)