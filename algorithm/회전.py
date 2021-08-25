for t in range(int(input())):
    n,m = map(int,input().split())
    queue = list(map(int,input().split()))
    front = 0
    rear = n
    cnt = 0
    for _ in range(m):
        queue.append(0)
    while cnt != m:
        res = queue[front]
        front += 1
        queue[rear] = res
        rear += 1
        cnt += 1
    print('#{} {}'.format(t+1,queue[front]))