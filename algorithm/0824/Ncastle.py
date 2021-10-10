cnt = 0
def dfs(level,N):
    if level == N:
        global cnt
        cnt += 1
        return
    for x in range(N):
        if used[x] == 1:
            continue
        map[level][x] = 1
        used[x] = 1
        dfs(level + 1,N)
        used[x] = 0
        map[level][x] = 0
    return
for t in range(1,11):
    N = int(input())
    map = [[0 for _ in range(N)] for _ in range(N)]
    used = list(0 for _ in range(N))
    dfs(0,N)
    print('#{} {}'.format(t,cnt))
    cnt = 0