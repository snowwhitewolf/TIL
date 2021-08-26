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
    print(stx,sty,resx,resy)
    dx = [-1,0,1,0]
    dy = [0, 1, 0, -1]
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((sty,stx))
    while queue:
        y,x = queue.popleft()
        if x == resx and y == resy:
            break
        for i in range(4):
            nextx = x + dx[i]
            nexty = y + dy[i]
            if 0 <= nextx < n and 0 <= nexty < n and maze[nexty][nextx] == 0 and visited[nexty][nextx]==0:
                queue.append((nexty,nextx))
                visited[nexty][nextx] = visited[sty][stx] + 1
    print(visited)