for t in range(int(input())):
    n = int(input())
    left = [0 for _ in range(n + 1)]
    right = [0 for _ in range(n + 1)]
    lst = []
    for i in range(n-1):
        lst.append(list(map(int,input().split())))

    left[lst[0][0]] = lst[0][1]
    for i in range(1,n-1):
        if lst[i][0] == lst[i-1][0]:
            right[lst[i][0]] = lst[i][1]
        else:
            left[lst[i][0]] = lst[i][1]
    res = []
    def dfs(now):
        if now == 0:
            return
        res.append(now)
        dfs(left[now])
        dfs(right[now])
    dfs(1)
    print('#{}'.format(t+1),end=' ')
    print(*res)