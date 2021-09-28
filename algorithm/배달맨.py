from collections import deque
for t in range(int(input())):
    h,w,n = map(int,input().split())
    lst = []
    for i in range(h):
        lst.append(list(input().rstrip()))
    cnt = 0
    stx = 0
    sty = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(y1, x1,num):
        global stx
        global sty
        visited = [[0] * w for _ in range(h)]
        queue = deque()
        queue.append((y1, x1))
        while queue:
            y, x = queue.popleft()
            if num > n:
                break
            for i in range(4):
                nextx = x + dx[i]
                nexty = y + dy[i]
                if 0 <= nextx < w and 0 <= nexty < h:
                    if lst[nexty][nextx] != '#' and visited[nexty][nextx] == 0:
                        queue.append((nexty, nextx))
                        visited[nexty][nextx] = visited[y][x] + 1
                    if lst[nexty][nextx] == str(num):
                        stx = nextx
                        sty = nexty
                        return visited[nexty][nextx]
    for k in range(1,n+1):
        cnt += bfs(sty,stx,k)
    print('#{} {}'.format(t + 1, cnt))