queue = [0,0,0,0,0,0,0,0,0,0]
front = 0
rear = 0
queue[rear] = 3
rear += 1
queue[rear] = 7
rear += 1
queue[rear] = 5
rear += 1
ret = queue[front]
print(ret)
front += 1
ret = queue[front]
print(ret)
front += 1