from collections import deque

lst = [[0]*8 for _ in range(8)]
lst[1][2] = 1
lst[1][3] = 1
lst[2][5] = 1
lst[4][2] = 1
lst[4][6] = 1
lst[5][6] = 1
lst[6][4] = 1
lst[7][6] = 1
lst[7][3] = 1
lst[3][7] = 1

visited = [0,1,0,0,0,0,0,0]

queue = deque()
queue.append(1)
while queue:
    now = queue.popleft()
    for next in range(8):
        if lst[now][next] == 1 and visited[next] <= 0:
            visited[next] = visited[now]+1
            queue.append(next)
            print('no.{} level{}'.format(now,visited[now]))
