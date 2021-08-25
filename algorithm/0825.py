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
for j in range(8):
    if lst[0][j] == 1:
        queue.append(j)
ret = queue.popleft()
for j in range(8):
    if lst[ret][j] == 1:
        queue.append(j)
print(queue)