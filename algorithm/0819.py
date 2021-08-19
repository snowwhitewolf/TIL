for t in range(int(input())):
    V, E = map(int, input().split())
    lst = list([0 for _ in range(V+1)] for _ in range(V+1))
    for e in range(E):
        a, b = map(int, input().split())
        lst[a][b] = 1
    gg = 0
    S, G = map(int, input().split())
    visited = list(0 for _ in range(V+1))
    def dfs(now):
        for next in range(1, V+1):
            if lst[now][next] == 1 and visited[next] == 0:
                if next == G:
                    global gg
                    gg = 1
                    break
                visited[next] = 1
                dfs(next)
        return

    dfs(S)
    print('#{} {}'.format(t+1,gg))
