import sys
sys.stdin= open('input.txt', "r")


def dfs(y, x, s):
    if y == N - 1 and x == N - 1:
        res.append(s+MAP[N-1][N-1])
        return
    if y + 1 < N:
        dfs(y + 1, x, s + MAP[y][x])
    if x + 1 < N:
        dfs(y, x + 1, s + MAP[y][x])

for t in range(int(input())):
    res = []
    N = int(input())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int,input().split())))
    dfs(0,0,0)
    print('#{} {}'.format(t+1,min(res)))