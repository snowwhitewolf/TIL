from collections import deque

value = [0,1,1,3,2,4,5,2]
lst = [[0] * 8 for _ in range(8)]
lst[0][1] = 1
lst[0][2] = 1
lst[0][3] = 1
lst[1][4] = 1
lst[1][5] = 1
lst[1][6] = 1
lst[3][7] = 1
queue = deque()
queue.append(0)
while queue:
    now = queue.popleft()
    print(now, end=' ')
    for next in range(8):
        if lst[now][next] == 1:
            queue.append(next)
