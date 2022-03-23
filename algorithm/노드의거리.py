from collections import deque

for t in range(int(input())):
    n, l = map(int,input().split())
    lst = [[0]*(n+1) for _ in range(n+1)]
    for i in range(l):
        now1, next1 = map(int,input().split())
        lst[now1][next1] = 1
        lst[next1][now1] = 1
    now2, next2 = map(int,input().split())

    def bfs(start, end, cnt):
        queue = deque()
        visited = [0 for _ in range(cnt + 1)]

        queue.append(start)
        visited[start] = 1

        while queue:
            now = queue.popleft()
            for next in range(1, cnt + 1):
                if lst[now][next] == 0:
                    continue
                if visited[next] > 0:
                    continue
                visited[next] = visited[now] + 1
                queue.append(next)
            if now == end:
                return visited[now]
        return 1

    result = bfs(now2,next2,n)
    print('#{} {}'.format(t+1,result-1))
