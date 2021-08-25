from collections import deque

for t in range(10):
    tc = input()
    lst = list(map(int,input().split()))
    pwd = deque()
    for i in range(8):
        pwd.append(lst[i])
    cnt = 1
    while True:
        next = pwd.popleft()
        if next-cnt <= 0:
            break
        else:
            pwd.append(next-cnt)
        cnt += 1
        if cnt == 6:
            cnt = 1
    pwd.append(0)
    result = []
    for i in range(8):
        result.append(pwd.popleft())

    print('#{}'.format(tc),end=' ')
    print(' '.join(i for i in result))