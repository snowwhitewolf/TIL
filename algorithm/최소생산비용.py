def func(level,cost,v):
    global res
    if level == N:
        if res > cost:
            res = cost
        return

    for i in range(N):
        if cost > res:
            break
        if str(i) in v:
            continue
        func(level+1,cost+lst[level][i],v+f'{i}')

for t in range(int(input())):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int,input().split())))
    res = 536568756345
    func(0,0,'')
    print('#{} {}'.format(t+1,res))
