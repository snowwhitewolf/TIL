import sys
sys.stdin = open('../1014/input.txt', 'r')


def point(s):
    global res
    f2 = []
    for l in range(N):
        if l not in s:
            f2.append(l)
    res = min(res, abs(cal(s) - cal(f2)))
    return

def dfs(level, prev, path):
    if level == N // 2:
        if len(path) == N//2:
            point(path)
        return
    for i in range(prev + 1, N):
        dfs(level + 1, i, path+[i])
    return

def cal(f1):
    f1s = 0
    for b in f1:
        for c in f1:
           f1s += lst[b][c]
    return f1s

for t in range(int(input())):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    res = 126454612321456

    dfs(0, -1, [])
    print('#{} {}'.format(t+1,res))
