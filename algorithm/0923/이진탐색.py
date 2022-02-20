for t in range(int(input())):
    N = int(input())
    lst = [0 for _ in range(N+1)]
    cnt = 1

    def dfs(now):
        global cnt
        if now >= N+1:
            return
        dfs(now * 2)  # left subtree
        lst[now] = cnt
        cnt += 1
        dfs(now * 2 + 1)  # right subtree
        return

    dfs(1)
    print('#{} {} {}'.format(t+1, lst[1], lst[N//2]))
