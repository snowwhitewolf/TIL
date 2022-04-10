def dfs(n,path):
    global res
    res = max(res,path)
    visited[n] = 1
    for j in lst[n]:
        if visited[j] == 0:
            dfs(j,path+1)
            visited[j] = 0

for t in range(int(input())):
    N, M = map(int,input().split())
    lst = [[] for _ in range(N+1)]
    res = 0
    for i in range(M):
        start,end = map(int,input().split())
        lst[start].append(end)
        lst[end].append(start)

    for n in range(1,N+1):
        visited = [0]*(N+1)
        dfs(n,1)
    print('#{} {}'.format(t+1,res))