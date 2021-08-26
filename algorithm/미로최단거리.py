from collections import deque
for t in range(int(input())):
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if maze[y][x] == 2:
                sty,stx = y, x
            elif maze[y][x] == 3:
                resy,resx = y, x
    dx = [-1,0,1,0]
    dy = [0, 1, 0, -1]
    def bfs(sty1,stx1):
        visited = [[0] * n for _ in range(n)]
        queue = deque()
        queue.append((sty1, stx1))
        while queue:
            y,x = queue.popleft()
            if x == resx and y == resy:
                break
            for i in range(4):
                nextx = x + dx[i]
                nexty = y + dy[i]
                if 0 <= nextx < n and 0 <= nexty < n:
                    if maze[nexty][nextx] == 0 and visited[nexty][nextx]==0:
                        queue.append((nexty, nextx))
                        visited[nexty][nextx] = visited[y][x] + 1
                    if maze[nexty][nextx] == 3:
                        return visited[y][x]
        return 0
    print('#{} {}'.format(t+1,bfs(sty,stx)))