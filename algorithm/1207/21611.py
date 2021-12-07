import sys
sys.stdin = open('input.txt', 'r')

N,M = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
boom = [list(map(int,input().split())) for _ in range(M)]
shark = N//2
by = [0,-1,1,0,0]
bx = [0,0,0,-1,1]
total = [0,0,0,0]
def blizzard(d,s):
    for ss in range(1,s+1):
        y = shark + by[d]*ss
        x = shark + bx[d]*ss
        MAP[y][x] = 0


dy = [0,1,0,-1]
dx = [-1,0,1,0]

y = shark
x = shark

for k in range(M):
    d = 0
    cnt = 1
    lst = []
    blizzard(boom[k][0], boom[k][1])
    while True:
        if y == 0 and x == 0:
            break
        for c in range(cnt):
            y +=  dy[d]
            x +=  dx[d]
            if y ==0 and x == 0:
                if MAP[y][x]:
                    lst.append(MAP[y][x])
                break
            if MAP[y][x]:
                lst.append(MAP[y][x])

        d += 1
        if d == 4:
            d = 0
        if y == 0 and x == 0:
            break
        for c in range(cnt):
            y +=  dy[d]
            x +=  dx[d]
            if y ==0 and x == 0:
                if MAP[y][x]:
                    lst.append(MAP[y][x])
                break
            if MAP[y][x]:
                lst.append(MAP[y][x])

        cnt += 1
        d += 1
        if d == 4:
            d = 0
    while True:
        cnt = 0
        ii=1
        for i in range(len(lst)):
            now = lst[i]
            while i+ii < len(lst) and lst[i+ii] == now:
                ii+=1
                cnt += 1
            if cnt >= 3:
                for j in range(cnt+1):
                    lst[i+j] = 0
                total[now] += cnt+1
            cnt = 0
            ii = 1
        lst2 = []
        for i in lst:
            if i:
                lst2.append(i)
        if lst == lst2:
            break
        lst = lst2

    lst2 = []
    while True:
        cnt = 0
        ii=1
        i=0
        while i < len(lst):
            now = lst[i]
            while i+ii < len(lst) and lst[i+ii] == now:
                ii+=1
                cnt += 1
            lst2.append(cnt + 1)
            lst2.append(lst[i])
            i = i + ii
            cnt = 0
            ii = 1
        break
    lst = lst2
    for i in range(N*N):
        lst.append(0)
    res = 0
    d = 0
    cnt = 1
    y = shark
    x = shark
    while res != N*N:
        if y == 0 and x == 0:
            break
        for c in range(cnt):
            y +=  dy[d]
            x +=  dx[d]
            if y ==0 and x == 0:
                MAP[y][x] = lst[res]
                res += 1
                break
            MAP[y][x] = lst[res]
            res += 1

        d += 1
        if d == 4:
            d = 0
        if y == 0 and x == 0:
            break
        for c in range(cnt):
            y +=  dy[d]
            x +=  dx[d]
            if y ==0 and x == 0:
                MAP[y][x] = lst[res]
                res += 1
                break
            MAP[y][x] = lst[res]
            res += 1
        cnt += 1
        d += 1
        if d == 4:
            d = 0
    for i in range(N):
        print(*MAP[i])
    print('-------------')
print(total[1]+total[2]*2+total[3]*3)


