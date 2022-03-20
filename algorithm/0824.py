adj = [
    [0,1,1,1],
    [1,0,0,1],
    [0,1,0,1],
    [0,0,0,0],
]

visited = [0,0,0,0]
def dfs(now,s) :
    if now == 3 :
        print(s)
        return
    for next in range(4):
        if adj[now][next] == 0 : continue # 연결점 찾기
        if visited[next] == 1 : continue  # next 가 이미 방문
        visited[next] = 1
        dfs(next,s+str(next))


visited[0] = 1
dfs(0,'')