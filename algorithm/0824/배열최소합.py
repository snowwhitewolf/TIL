def dfs(level,N,res):
    if level == N:
        global cnt
        cnt = min(cnt,res)
        return
    for x in range(N):
        if used[x] == 1:
            continue
        res+= lst[level][x]
        used[x] = 1
        dfs(level + 1,N,res)
        used[x] = 0
        res -= lst[level][x]
    return
for t in range(int(input())):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int,input().split())))
    used = list(0 for _ in range(N))
    cnt = 100000
    dfs(0,N,0)
    print('#{} {}'.format(t+1,cnt))