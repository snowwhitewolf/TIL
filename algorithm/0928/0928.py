def dfs(y, x):
    global cnt
    if lst[y][x] == 0:
        return
    if lst[y][x] == 2:
        lst[y][x] = 1
    if visited[y][x] == 1:
        return

    visited[y][x] = 1
    dfs(y - 1, x)
    dfs(y + 1, x)
    dfs(y, x - 1)
    dfs(y, x + 1)
    return

for t in range(int(input())):
    n,m = map(int,input().split())
    lst = list()
    lst.append([0 for _ in range(m+2)])
    for i in range(n):
        lst.append([0] + list(map(int,input().split()))+[0])
    lst.append([0 for _ in range(m+2)])
    cnt = 0
    visited = [[0] * len(lst[0]) for _ in range(n+2)]

    for y in range(1,n+1):
        for x in range(1,m+1):
            if lst[y][x] == 2:
                dfs(y, x)
                cnt += 1
    print('#{} {}'.format(t+1, cnt))