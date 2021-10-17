from collections import deque

value = [0,1,1,3,2,4,5,2]
lst = [[0] * 5 for _ in range(5)]
lst[0][1] = 1
lst[0][2] = 1
lst[1][3] = 1
lst[1][4] = 1
lst[2][1] = 1
lst[2][3] = 1
lst[4][2] = 1
queue = deque()
queue.append(0)
while queue:
    now = queue.popleft()
    print(value[now],end = ' ')
    for next in range(8):
        if lst[now][next] == 1:
            queue.append(next)