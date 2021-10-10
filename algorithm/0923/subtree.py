for t in range(int(input())):
    E,N = map(int,input().split())
    lst = list(map(int,(input().split())))
    left = [0 for _ in range(E+2)]
    right = [0 for _ in range(E+2)]
    cnt = 0
    for i in range(0,E*2-1,2):
        if left[lst[i]] == 0:
            left[lst[i]] = lst[i+1]
        else:
            right[lst[i]] = lst[i+1]
    def dfs(now):
        global cnt
        if now == 0:
            return
        dfs(left[now])
        cnt += 1
        dfs(right[now])
    dfs(N)
    print('#{} {}'.format(t+1,cnt))
