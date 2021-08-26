from collections import deque

for t in range(int(input())):
    n,m = map(int,input().split())
    pizza = list(map(int,input().split()))
    lst = []
    for i in range(len(pizza)):
        lst.append(pizza[i])
        lst.append(i+1)
    queue = deque()
    for p in range(n*2):
        queue.append(lst.pop(0))
    while len(queue) > 2:
        for i in range(n):
            if len(queue) != 2:
                now = queue.popleft()
                num = queue.popleft()
                if now//2 != 0:
                    queue.append(now//2)
                    queue.append(num)
                elif len(lst)!=0:
                    queue.append(lst.pop(0))
                    queue.append(lst.pop(0))
                else:
                    continue
            else:
                break
    queue.popleft()
    result = queue.popleft()
    print('#{} {}'.format(t+1,result))