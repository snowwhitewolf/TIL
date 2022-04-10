import sys
sys.stdin = open("input.txt",'r')


def func(level, p):
    global res
    if p <= res:
        return
    if level == N:
        res = p
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            func(level + 1, p * lst[level][i])
            visit[i] = 0

for t in range(1,int(input())+1):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int,input().split())))
        for j in range(N):
            lst[i][j] /= 100
    res = 0
    visit = [0]*N
    func(0,100)
    print('#{} {:6f}'.format(t, res))